import ctypes
import platform
import zipfile
import os
from .abf import parser
from .abf.data_model import DataModel


class PbixUnpacker:
    def __init__(self, file_path):
        self.file_path = file_path

        # Attributes populated during unpacking
        self._data_model = DataModel(file_log=[], decompressed_data=b'')
        
        # Setup library
        self.__setup_library()
        
        # Trigger unpacking upon instantiation
        self.__unpack()

    def __setup_library(self):
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Determine the path to the shared library based on the platform
        if platform.system() == "Windows":
            self.lib_path = os.path.join(current_dir, '..', 'lib', 'libxpress9.dll')
        elif platform.system() == "Linux":
            self.lib_path = os.path.join(current_dir, '..', 'lib', 'libxpress9.so')
        elif platform.system() == "Darwin":
            self.lib_path = os.path.join(current_dir, '..', 'lib', 'libxpress9.dylib')
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

    def __unpack(self):
        # Initialize the library
        result = self.lib.Initialize()
        if result:
            raise RuntimeError("Failed to initialize the library")
        
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            # Open the DataModel file within the ZIP
            with zip_ref.open('DataModel') as data_model_in_pbix:

                all_decompressed_data = bytearray()
                total_size = data_model_in_pbix.seek(0, 2)  # Get total size of file
                data_model_in_pbix.seek(102)  # Signature: This backup was created using Xpress9 compression.

                while data_model_in_pbix.tell() < total_size:
                    uncompressed_size = int.from_bytes(data_model_in_pbix.read(4), 'little')  # Read uint32 for uncompressed size
                    compressed_size = int.from_bytes(data_model_in_pbix.read(4), 'little')  # Read uint32 for compressed size
                    compressed_data = data_model_in_pbix.read(compressed_size)

                    # Create ctypes buffers
                    compressed_buffer = (ctypes.c_ubyte * compressed_size)(*compressed_data)
                    decompressed_buffer = (ctypes.c_ubyte * uncompressed_size)()

                    # Decompress the data
                    decompressed_size = self.lib.Decompress(compressed_buffer, compressed_size, decompressed_buffer, uncompressed_size)
                    if decompressed_size != uncompressed_size:
                        raise RuntimeError(f"Expected {uncompressed_size} bytes after decompression, but got {decompressed_size} bytes")

                    # Append decompressed data to all_decompressed_data
                    all_decompressed_data.extend(decompressed_buffer)

        # Terminate the library
        self.lib.Terminate()

        # Populate the byte array of the data bundle
        self._data_model.decompressed_data = all_decompressed_data

        # Parse the decompressed data
        abf_parser = parser.AbfParser(self._data_model)


    @property
    def data_model(self):
        return self._data_model

    @data_model.setter
    def data_model(self, value):
        if isinstance(value, DataModel):
            self._data_model = value
        else:
            raise ValueError("Expected an instance of DataModel.")