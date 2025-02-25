import ctypes
import platform
import zipfile
import os
from .abf import parser
from .abf.data_model import DataModel


class PbixUnpacker:
    # Constants for file signatures
    SINGLE_THREAD_SIGNATURE = "This backup was created using XPress9 compression."
    MULTI_THREAD_SIGNATURE = "This backup was created using multithreaded XPrs9."
    STREAM_STORAGE_SIGNATURE = b'\xff\xfe' + "STREAM_STORAGE_SIGNATURE_)!@#$%^&*(".encode('utf-16le')

    def __init__(self, file_path):
        self.file_path = file_path

        # Attributes populated during unpacking
        self._data_model = DataModel(file_log=[], decompressed_data=b'')
        
        # Setup library
        self.__setup_library()
        
        # Detect file type and unpack accordingly
        self.__unpack()

    def __setup_library(self):
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Determine the path to the shared library based on the platform
        if platform.system() == "Windows":
            self.lib_path = os.path.join(current_dir, 'lib', 'libxpress9.dll')
        elif platform.system() == "Linux":
            self.lib_path = os.path.join(current_dir, 'lib', 'libxpress9.so')
        elif platform.system() == "Darwin":
            self.lib_path = os.path.join(current_dir, 'lib', 'libxpress9.dylib')
        else:
            raise RuntimeError("Unsupported platform")

        # Load the shared library
        self.lib = ctypes.CDLL(self.lib_path)

        # Define the function signatures
        self.lib.Initialize.argtypes = []
        self.lib.Initialize.restype = ctypes.c_bool

        self.lib.Decompress.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int]
        self.lib.Decompress.restype = ctypes.c_uint

        self.lib.Terminate.argtypes = []
        self.lib.Terminate.restype = None

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
        # Initialize the library
        result = self.lib.Initialize()
        if result:
            raise RuntimeError("Failed to initialize the library")
        
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

        # Terminate the library
        self.lib.Terminate()

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

        while data_model_file.tell() < total_size:
            uncompressed_size = int.from_bytes(data_model_file.read(4), 'little')  # Read uint32 for uncompressed size
            compressed_size = int.from_bytes(data_model_file.read(4), 'little')  # Read uint32 for compressed size
            compressed_data = data_model_file.read(compressed_size)

            # Create ctypes buffers
            compressed_buffer = (ctypes.c_ubyte * compressed_size)(*compressed_data)
            decompressed_buffer = (ctypes.c_ubyte * uncompressed_size)()

            # Decompress the data
            decompressed_size = self.lib.Decompress(compressed_buffer, compressed_size, decompressed_buffer, uncompressed_size)
            if decompressed_size != uncompressed_size:
                raise RuntimeError(f"Expected {uncompressed_size} bytes after decompression, but got {decompressed_size} bytes")

            # Append decompressed data
            all_decompressed_data.extend(decompressed_buffer)
            
        # Populate the byte array of the data bundle
        self._data_model.decompressed_data = all_decompressed_data

    def __process_multi_threaded(self, data_model_file):
        """Process a multi-threaded Xpress9 compressed DataModel file."""
        all_decompressed_data = bytearray()
        
        # Skip signature
        data_model_file.seek(102)
        
        # Read thread distribution information
        main_chunks_per_thread = int.from_bytes(data_model_file.read(8), 'little')
        prefix_chunks_per_thread = int.from_bytes(data_model_file.read(8), 'little')
        prefix_thread_count = int.from_bytes(data_model_file.read(8), 'little')
        main_thread_count = int.from_bytes(data_model_file.read(8), 'little')
        chunk_uncompressed_size = int.from_bytes(data_model_file.read(8), 'little')
        
        # Calculate total expected chunks
        total_chunks = (main_chunks_per_thread * main_thread_count) + (prefix_chunks_per_thread * prefix_thread_count)
        
        # Process all prefix chunks
        for _ in range(prefix_thread_count):
            for _ in range(prefix_chunks_per_thread):
                uncompressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_data = data_model_file.read(compressed_size)

                # Create ctypes buffers
                compressed_buffer = (ctypes.c_ubyte * compressed_size)(*compressed_data)
                decompressed_buffer = (ctypes.c_ubyte * uncompressed_size)()

                # Decompress the data
                decompressed_size = self.lib.Decompress(compressed_buffer, compressed_size, decompressed_buffer, uncompressed_size)
                if decompressed_size != uncompressed_size:
                    raise RuntimeError(f"Expected {uncompressed_size} bytes after decompression, but got {decompressed_size} bytes")

                # Append decompressed data
                all_decompressed_data.extend(decompressed_buffer)
            self.lib.Terminate()
            self.lib.Initialize()
        
        # Process all main chunks
        for _ in range(main_thread_count):
            for _ in range(main_chunks_per_thread):
                uncompressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_size = int.from_bytes(data_model_file.read(4), 'little')
                compressed_data = data_model_file.read(compressed_size)

                # Create ctypes buffers
                compressed_buffer = (ctypes.c_ubyte * compressed_size)(*compressed_data)
                decompressed_buffer = (ctypes.c_ubyte * uncompressed_size)()

                # Decompress the data
                decompressed_size = self.lib.Decompress(compressed_buffer, compressed_size, decompressed_buffer, uncompressed_size)
                if decompressed_size != uncompressed_size:
                    raise RuntimeError(f"Expected {uncompressed_size} bytes after decompression, but got {decompressed_size} bytes")

                # Append decompressed data
                all_decompressed_data.extend(decompressed_buffer)
            self.lib.Terminate()
            self.lib.Initialize()
            
        # Populate the byte array of the data bundle
        self._data_model.decompressed_data = all_decompressed_data

    @property
    def data_model(self):
        return self._data_model

    @data_model.setter
    def data_model(self, value):
        if isinstance(value, DataModel):
            self._data_model = value
        else:
            raise ValueError("Expected an instance of DataModel.")