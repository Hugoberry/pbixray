import ctypes
import platform
import os


class Xpress9Library:
    """
    A class that handles the loading, initialization, usage, and cleanup of the xpress9 compression library.
    """
    
    def __init__(self):
        """Initialize the xpress9 library attributes without loading."""
        self.lib = None
        self.lib_path = None
        self._setup_library()
        
    def _setup_library(self):
        """Set up the xpress9 library based on the current platform."""
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

        self.lib.Decompress.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, 
                                       ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int]
        self.lib.Decompress.restype = ctypes.c_uint

        self.lib.Terminate.argtypes = []
        self.lib.Terminate.restype = None
        

            
    def decompress(self, compressed_data, compressed_size, uncompressed_size):
        """
        Decompress data using the xpress9 library.
        
        Args:
            compressed_data (bytes): The compressed data.
            compressed_size (int): Size of the compressed data.
            uncompressed_size (int): Expected size of the uncompressed data.
            
        Returns:
            bytearray: Decompressed data.
            
        Raises:
            RuntimeError: If decompression fails or size mismatch occurs.
        """
        # Create ctypes buffers
        compressed_buffer = (ctypes.c_ubyte * compressed_size)(*compressed_data)
        decompressed_buffer = (ctypes.c_ubyte * uncompressed_size)()

        # Decompress the data
        decompressed_size = self.lib.Decompress(compressed_buffer, compressed_size, 
                                               decompressed_buffer, uncompressed_size)
        
        if decompressed_size != uncompressed_size:
            raise RuntimeError(f"Expected {uncompressed_size} bytes after decompression, "
                              f"but got {decompressed_size} bytes")

        # Convert to bytearray and return
        return bytearray(decompressed_buffer)
    
    def initialize(self):
        """Initialize the xpress9 library."""
        result = self.lib.Initialize()
        if result:
            raise RuntimeError("Failed to initialize the xpress9 library")
    
    def terminate(self):
        """Terminate the xpress9 library."""
        if self.lib:
            self.lib.Terminate()
        
    def __del__(self):
        """Clean up resources when the object is destroyed."""
        if self.lib:
            self.lib.Terminate()