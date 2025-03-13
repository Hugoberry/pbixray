import ctypes
from ctypes import wintypes
import os

# Load necessary DLLs
cabdll = ctypes.WinDLL('cabinet.dll')

# Constants
COMPRESS_ALGORITHM_MSZIP = 2
COMPRESS_ALGORITHM_XPRESS = 3
COMPRESS_ALGORITHM_XPRESS_HUFF = 4
COMPRESS_ALGORITHM_LZMS = 5
COMPRESSION_FORMAT_DEFAULT = 0
COMPRESSION_ENGINE_MAXIMUM = 0x0100

# Set up CreateCompressor function
CreateCompressor = ctypes.windll.cabinet.CreateCompressor
CreateCompressor.restype = wintypes.BOOL
CreateCompressor.argtypes = [
    wintypes.DWORD,    # Algorithm 
    wintypes.LPVOID,   # AllocationRoutines (NULL for default)
    ctypes.POINTER(wintypes.HANDLE)  # CompressorHandle
]

# Set up Compress function
cabdll.Compress.restype = wintypes.BOOL
cabdll.Compress.argtypes = [
    wintypes.HANDLE,   # CompressorHandle
    wintypes.LPVOID,   # UncompressedData
    wintypes.DWORD,    # UncompressedDataSize
    wintypes.LPVOID,   # CompressedBuffer
    wintypes.DWORD,    # CompressedBufferSize
    ctypes.POINTER(wintypes.DWORD)  # CompressedDataSize
]

# Set up CloseCompressor function
CloseCompressor = ctypes.windll.cabinet.CloseCompressor
CloseCompressor.restype = wintypes.BOOL
CloseCompressor.argtypes = [
    wintypes.HANDLE    # CompressorHandle
]

# Set up CreateDecompressor function
CreateDecompressor = ctypes.windll.cabinet.CreateDecompressor
CreateDecompressor.restype = wintypes.BOOL
CreateDecompressor.argtypes = [
    wintypes.DWORD,    # Algorithm
    wintypes.LPVOID,   # AllocationRoutines (NULL for default)
    ctypes.POINTER(wintypes.HANDLE)  # DecompressorHandle
]

# Set up Decompress function
cabdll.Decompress.restype = wintypes.BOOL
cabdll.Decompress.argtypes = [
    wintypes.HANDLE,   # DecompressorHandle
    wintypes.LPVOID,   # CompressedData
    wintypes.DWORD,    # CompressedDataSize
    wintypes.LPVOID,   # UncompressedBuffer
    wintypes.DWORD,    # UncompressedBufferSize
    ctypes.POINTER(wintypes.DWORD)  # UncompressedDataSize
]

# Set up CloseDecompressor function
CloseDecompressor = ctypes.windll.cabinet.CloseDecompressor
CloseDecompressor.restype = wintypes.BOOL
CloseDecompressor.argtypes = [
    wintypes.HANDLE    # DecompressorHandle
]

def get_last_error_message():
    error_code = ctypes.windll.kernel32.GetLastError()
    return f"Error code: {error_code}"

# File paths
input_file_path = "data/output/metadata.sqlitedb"
output_file_path = "out.bin"

# Read the input file
print(f"Reading file: {input_file_path}")
with open(input_file_path, "rb") as f:
    input_data = f.read()

input_size = len(input_data)
print(f"File size: {input_size} bytes")

# Create a compressor handle
compressor_handle = wintypes.HANDLE()
success = CreateCompressor(
    COMPRESS_ALGORITHM_XPRESS,  # Compression algorithm
    None,                            # Use default allocation
    ctypes.byref(compressor_handle)  # Compressor handle
)

if not success:
    raise RuntimeError(f"Failed to create compressor: {get_last_error_message()}")

try:
    # Allocate buffer for compressed data
    # For Xpress Huffman, worst case is about original size + overhead
    compressed_buffer_size = input_size + 1024  # Add extra space for safety
    compressed_buffer = ctypes.create_string_buffer(compressed_buffer_size)
    compressed_size = wintypes.DWORD()

    # Compress Data
    print("Compressing file...")
    success = cabdll.Compress(
        compressor_handle,            # Compressor handle
        input_data,                   # Uncompressed data
        input_size,                   # Uncompressed size
        compressed_buffer,            # Compressed buffer
        compressed_buffer_size,       # Compressed buffer size
        ctypes.byref(compressed_size) # Compressed size output
    )

    if not success:
        raise RuntimeError(f"Compression failed: {get_last_error_message()}")

    compression_ratio = (compressed_size.value / input_size) * 100
    print(f"Original Size: {input_size:,} bytes")
    print(f"Compressed Size: {compressed_size.value:,} bytes")
    print(f"Compression Ratio: {compression_ratio:.2f}%")

    # Write the compressed data to the output file
    print(f"Writing compressed data to: {output_file_path}")
    with open(output_file_path, "wb") as f:
        f.write(compressed_buffer.raw[:compressed_size.value])
    
    print(f"Successfully compressed file to {output_file_path}")

    # Optional: Verify the compression by decompressing and checking
    verify = input("Would you like to verify the compression? (y/n): ").lower().strip() == 'y'
    
    if verify:
        # Create a decompressor handle
        decompressor_handle = wintypes.HANDLE()
        success = CreateDecompressor(
            COMPRESS_ALGORITHM_XPRESS,    # Decompression algorithm
            None,                              # Use default allocation
            ctypes.byref(decompressor_handle)  # Decompressor handle
        )

        if not success:
            raise RuntimeError(f"Failed to create decompressor: {get_last_error_message()}")

        try:
            # Allocate buffer for decompression
            decompressed_buffer = ctypes.create_string_buffer(input_size)
            decompressed_size = wintypes.DWORD(input_size)

            # Read the compressed data back
            with open(output_file_path, "rb") as f:
                compressed_data = f.read()
                
            # Create a C buffer for the compressed data
            compressed_c_buffer = ctypes.create_string_buffer(compressed_data)

            # Decompress Data
            print("Verifying by decompressing...")
            success = cabdll.Decompress(
                decompressor_handle,           # Decompressor handle
                compressed_c_buffer,           # Compressed data
                len(compressed_data),          # Compressed size
                decompressed_buffer,           # Decompressed buffer
                input_size,                    # Decompressed buffer size
                ctypes.byref(decompressed_size) # Decompressed size output
            )

            if not success:
                raise RuntimeError(f"Decompression failed: {get_last_error_message()}")

            # Verify if decompressed data matches the original
            result = decompressed_buffer.raw[:decompressed_size.value]
            if result == input_data:
                print("Verification successful! Decompressed data matches original.")
                print(f"Decompressed Size: {decompressed_size.value:,} bytes")
            else:
                print("Verification failed! Decompressed data does not match original.")
                
        finally:
            # Always close the decompressor handle
            CloseDecompressor(decompressor_handle)
finally:
    # Always close the compressor handle
    CloseCompressor(compressor_handle)