import shutil
import tempfile
import zipfile
import concurrent.futures
from .abf import parser
from .abf.data_model import DataModel, Container
from .abf.mapped_buffer import MappedBuffer
from .connections import parse_connections
from .exceptions import LiveConnectionError, NoEmbeddedModelError
from xpress9 import Xpress9


class _MemorySink:
    """Accumulates decompressed chunks into an in-process ``bytearray``.

    This preserves the original (``on_disk=False``) behavior byte-for-byte: the
    full decompressed data model lives in RAM for the lifetime of the loader.
    """

    def __init__(self):
        self._buf = bytearray()

    def write(self, chunk):
        self._buf.extend(chunk)

    def finish(self):
        return self._buf


class _FileSink:
    """Streams decompressed chunks to a temp file, then mmaps it (``on_disk=True``).

    Chunks are written as they are produced so the full decompressed data model
    is never held in RAM. :meth:`finish` returns a :class:`MappedBuffer` that owns
    the temp file and releases it on ``close()`` / GC.
    """

    def __init__(self, temp_dir=None):
        self._tmp = tempfile.NamedTemporaryFile(
            mode='wb', suffix='.pbixray', dir=temp_dir, delete=False
        )
        self._path = self._tmp.name

    def write(self, chunk):
        self._tmp.write(chunk)

    def finish(self):
        self._tmp.flush()
        self._tmp.close()
        return MappedBuffer(self._path)


class DataModelLoader:
    # Constants for file signatures
    SINGLE_THREAD_SIGNATURE = "This backup was created using XPress9 compression."
    MULTI_THREAD_SIGNATURE = "This backup was created using multithreaded XPrs9."
    STREAM_STORAGE_SIGNATURE = b'\xff\xfe' + "STREAM_STORAGE_SIGNATURE_)!@#$%^&*(".encode('utf-16le')

    def __init__(self, file_path, on_disk=False, temp_dir=None):
        self.file_path = file_path
        self._on_disk = on_disk
        self._temp_dir = temp_dir

        # Attributes populated during unpacking
        self._data_model = DataModel(file_log=[], decompressed_data=b'', container=Container.PBIX)
        self._connections = []
        self._data_mashup_bytes = None

        # Detect container and unpack accordingly
        self.__unpack()

    def __make_sink(self):
        """Create the output sink for decompressed data based on ``on_disk``."""
        return _FileSink(self._temp_dir) if self._on_disk else _MemorySink()

    def __detect_compression(self, data_model_file):
        """Detect the compression scheme of the DataModel stream based on its signature."""
        # Check for uncompressed ABF backup first (by looking at first 72 bytes)
        data_model_file.seek(0)
        stream_storage_sig = data_model_file.read(72)
        if self.STREAM_STORAGE_SIGNATURE in stream_storage_sig:
            return "uncompressed"
        
        # Check for compressed file type
        data_model_file.seek(0)
        signature = data_model_file.read(102)
        try:
            # Try to decode as UTF-16LE for compressed files
            decoded_sig = signature.decode('utf-16le', errors='ignore')
            if self.SINGLE_THREAD_SIGNATURE in decoded_sig:
                return "single_threaded"
            elif self.MULTI_THREAD_SIGNATURE in decoded_sig:
                return "multi_threaded"
        except:
            pass
        
        return "unknown"

    def __get_data_model_path(self, zip_ref):
        """Determine the path to the data model entry and set the container type."""
        if 'DataModel' in zip_ref.namelist():
            self._data_model.container = Container.PBIX
            return 'DataModel'

        if 'xl/model/item.data' in zip_ref.namelist():
            self._data_model.container = Container.XLSX
            return 'xl/model/item.data'

        # No embedded model. If the report carries a connection manifest it is a
        # thin/live-connection report whose model lives on an external server.
        if self._connections:
            raise LiveConnectionError(self._connections)
        raise NoEmbeddedModelError(
            "No supported data model found. File must be a PBIX with 'DataModel' "
            "or an XLSX with 'xl/model/item.data'."
        )

    def __unpack(self):
        # A pbix/xlsx is a zip envelope around the DataModel stream; a raw ``.abf``
        # Analysis Services backup is that same stream with no envelope. Branch on
        # the container so both reach the shared decompress + parse pipeline.
        if zipfile.is_zipfile(self.file_path):
            self.__unpack_zip()
        else:
            self.__unpack_abf()

        # Parse the decompressed data
        parser.AbfParser(self._data_model)

    def __unpack_zip(self):
        """Unpack a zip container (pbix/xlsx): connections, mashup, DataModel member."""
        # ``is_zipfile`` consumed/seeked a file-like ``file_path``; ZipFile re-seeks
        # from 0 itself, so no manual rewind is needed here.
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            self._connections = parse_connections(zip_ref)
            if 'DataMashup' in zip_ref.namelist():
                self._data_mashup_bytes = zip_ref.read('DataMashup')
            data_model_path = self.__get_data_model_path(zip_ref)

            with zip_ref.open(data_model_path) as data_model_in_archive:
                self.__decompress_stream(data_model_in_archive)

    def __unpack_abf(self):
        """Unpack a raw ``.abf`` backup: the DataModel stream with no zip envelope.

        An abf always carries an embedded model (sqlitedb-backed, like a pbix), so
        there are no connections or DataMashup to parse; the container stays PBIX.
        """
        self._data_model.container = Container.PBIX
        if hasattr(self.file_path, 'read'):
            self.file_path.seek(0)
            self.__decompress_stream(self.file_path)
        else:
            with open(self.file_path, 'rb') as data_model_file:
                self.__decompress_stream(data_model_file)

    def __decompress_stream(self, data_model_file):
        """Detect the DataModel stream's compression and emit it into a sink.

        Shared by the zip and raw-abf paths; ``on_disk`` only changes where the
        decompressed output lands, not how the stream is parsed.
        """
        compression = self.__detect_compression(data_model_file)
        if compression == "uncompressed":
            self.__process_uncompressed(data_model_file)
        elif compression == "single_threaded":
            self.__process_single_threaded(data_model_file)
        elif compression == "multi_threaded":
            self.__process_multi_threaded(data_model_file)
        else:
            raise RuntimeError("Unknown or unsupported DataModel compression format")

    def __process_uncompressed(self, data_model_file):
        """Process an uncompressed DataModel file."""
        sink = self.__make_sink()
        # Stream the member straight into the sink rather than reading it whole.
        data_model_file.seek(0)
        shutil.copyfileobj(data_model_file, sink)
        self._data_model.decompressed_data = sink.finish()

    def __process_single_threaded(self, data_model_file):
        """Process a single-threaded Xpress9 compressed DataModel file."""
        sink = self.__make_sink()
        total_size = data_model_file.seek(0, 2)  # Get total size of file
        data_model_file.seek(102)  # Skip signature

        # Create and initialize the xpress9 library
        xpress9_lib = Xpress9()
        try:
            while data_model_file.tell() < total_size:
                uncompressed_size = int.from_bytes(data_model_file.read(4), 'little')  # Read uint32 for uncompressed size
                compressed_size = int.from_bytes(data_model_file.read(4), 'little')  # Read uint32 for compressed size
                compressed_data = data_model_file.read(compressed_size)

                # Use the xpress9_lib to decompress
                decompressed_chunk = xpress9_lib.decompress(
                    compressed_data, uncompressed_size
                )

                # Emit decompressed data (RAM bytearray or temp file)
                sink.write(decompressed_chunk)
        finally:
            # Ensure the library is properly terminated
            del xpress9_lib

        # Populate the data bundle (bytearray or mmap-backed buffer)
        self._data_model.decompressed_data = sink.finish()

    def __process_multi_threaded(self, data_model_file):
        sink = self.__make_sink()
        data_model_file.seek(102)

        main_chunks_per_thread = int.from_bytes(data_model_file.read(8), 'little')
        prefix_chunks_per_thread = int.from_bytes(data_model_file.read(8), 'little')
        prefix_thread_count = int.from_bytes(data_model_file.read(8), 'little')
        main_thread_count = int.from_bytes(data_model_file.read(8), 'little')
        chunk_uncompressed_size = int.from_bytes(data_model_file.read(8), 'little')

        # Process prefix chunks if there are any
        if prefix_thread_count > 0 and prefix_chunks_per_thread > 0:
            # Read all prefix chunks and group by thread
            prefix_chunks = []
            for _ in range(prefix_thread_count * prefix_chunks_per_thread):
                uncompressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_data = data_model_file.read(compressed_size)
                prefix_chunks.append((uncompressed_size, compressed_data))

            prefix_groups = [prefix_chunks[i*prefix_chunks_per_thread : (i+1)*prefix_chunks_per_thread]
                            for i in range(prefix_thread_count)]

            # Process prefix groups in parallel, maintaining order
            if prefix_thread_count > 0:  # Ensure we only create a ThreadPoolExecutor if we have threads
                with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, prefix_thread_count)) as executor:
                    future_to_group = {executor.submit(self.__process_chunk_group, group): idx 
                                    for idx, group in enumerate(prefix_groups)}
                    # Collect results in original order
                    ordered_results = [None] * len(prefix_groups)
                    for future in concurrent.futures.as_completed(future_to_group):
                        idx = future_to_group[future]
                        ordered_results[idx] = future.result()
                    
                    for result in ordered_results:
                        if result:
                            sink.write(result)
        
        # Process main chunks if there are any
        if main_thread_count > 0 and main_chunks_per_thread > 0:
            # Read all main chunks and group by thread
            main_chunks = []
            for _ in range(main_thread_count * main_chunks_per_thread):
                uncompressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_data = data_model_file.read(compressed_size)
                main_chunks.append((uncompressed_size, compressed_data))

            main_groups = [main_chunks[i*main_chunks_per_thread : (i+1)*main_chunks_per_thread]
                        for i in range(main_thread_count)]

            # Process main groups in parallel, maintaining order
            if main_thread_count > 0:  # Ensure we only create a ThreadPoolExecutor if we have threads
                with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, main_thread_count)) as executor:
                    future_to_group = {executor.submit(self.__process_chunk_group, group): idx 
                                    for idx, group in enumerate(main_groups)}
                    # Collect results in original order
                    ordered_results = [None] * len(main_groups)
                    for future in concurrent.futures.as_completed(future_to_group):
                        idx = future_to_group[future]
                        ordered_results[idx] = future.result()
                    
                    for result in ordered_results:
                        if result:
                            sink.write(result)

        self._data_model.decompressed_data = sink.finish()

    def __process_chunk_group(self, chunk_group):
        if not chunk_group:
            return bytearray()
            
        xpress9_lib = Xpress9()
        decompressed = bytearray()
        try:
            for uncompressed_size, compressed_data in chunk_group:
                decompressed_chunk = xpress9_lib.decompress(
                    compressed_data, uncompressed_size
                )
                decompressed.extend(decompressed_chunk)
        finally:
            del xpress9_lib
        return decompressed

    @property
    def connections(self):
        """Parsed ``Connections`` manifest entries (list of dicts)."""
        return self._connections

    @property
    def data_mashup_bytes(self):
        """Raw bytes of the ``DataMashup`` part, or ``None`` when absent."""
        return self._data_mashup_bytes

    @property
    def data_model(self):
        return self._data_model

    @data_model.setter
    def data_model(self, value):
        if isinstance(value, DataModel):
            self._data_model = value
        else:
            raise ValueError("Expected an instance of DataModel.")