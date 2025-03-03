import zipfile
import concurrent.futures
from .abf import parser
from .abf.data_model import DataModel
from xpress9 import Xpress9


class PbixUnpacker:
    # Constants for file signatures
    SINGLE_THREAD_SIGNATURE = "This backup was created using XPress9 compression."
    MULTI_THREAD_SIGNATURE = "This backup was created using multithreaded XPrs9."
    STREAM_STORAGE_SIGNATURE = b'\xff\xfe' + "STREAM_STORAGE_SIGNATURE_)!@#$%^&*(".encode('utf-16le')

    def __init__(self, file_path):
        self.file_path = file_path

        # Attributes populated during unpacking
        self._data_model = DataModel(file_log=[], decompressed_data=b'')
        
        # Detect file type and unpack accordingly
        self.__unpack()

    def __detect_file_type(self, data_model_file):
        """Detect the type of DataModel file based on its signature."""
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

    def __unpack(self):
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            # Open the DataModel file within the ZIP
            with zip_ref.open('DataModel') as data_model_in_pbix:
                file_type = self.__detect_file_type(data_model_in_pbix)
                
                if file_type == "uncompressed":
                    self.__process_uncompressed(data_model_in_pbix)
                elif file_type == "single_threaded":
                    self.__process_single_threaded(data_model_in_pbix)
                elif file_type == "multi_threaded":
                    self.__process_multi_threaded(data_model_in_pbix)
                else:
                    raise RuntimeError("Unknown or unsupported DataModel file format")

        # Parse the decompressed data
        parser.AbfParser(self._data_model)

    def __process_uncompressed(self, data_model_file):
        """Process an uncompressed DataModel file."""
        # For uncompressed files, we can just read the entire file
        data_model_file.seek(0)
        all_data = data_model_file.read()
        self._data_model.decompressed_data = bytearray(all_data)

    def __process_single_threaded(self, data_model_file):
        """Process a single-threaded Xpress9 compressed DataModel file."""
        all_decompressed_data = bytearray()
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
                
                # Append decompressed data
                all_decompressed_data.extend(decompressed_chunk)
        finally:
            # Ensure the library is properly terminated
            del xpress9_lib
            
        # Populate the byte array of the data bundle
        self._data_model.decompressed_data = all_decompressed_data

    def __process_multi_threaded(self, data_model_file):
        all_decompressed_data = bytearray()
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
                            all_decompressed_data.extend(result)
        
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
                            all_decompressed_data.extend(result)

        self._data_model.decompressed_data = all_decompressed_data

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
    def data_model(self):
        return self._data_model

    @data_model.setter
    def data_model(self, value):
        if isinstance(value, DataModel):
            self._data_model = value
        else:
            raise ValueError("Expected an instance of DataModel.")