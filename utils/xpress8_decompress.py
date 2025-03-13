def xpress8_decompress(input_file, output_file):
    """
    Decompress a file that is structured as a series of compressed chunks.
    Each chunk starts with a 4-byte header:
    - First 2 bytes (uint16): Size of the uncompressed chunk
    - Next 2 bytes (uint16): Size of the compressed chunk
    
    Args:
        input_file (str): Path to the compressed input file
        output_file (str): Path to write the decompressed output
    
    Returns:
        int: Total size of decompressed data in bytes
    """
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            total_decompressed_size = 0
            
            # Process all chunks until end of file
            while True:
                # Read chunk header (4 bytes)
                header = f_in.read(4)
                if not header or len(header) < 4:
                    break  # End of file or incomplete header
                
                # Extract uncompressed and compressed sizes from header
                uncompressed_size = header[0] | (header[1] << 8)
                compressed_size = header[2] | (header[3] << 8)
                
                print(f"Chunk: uncompressed={uncompressed_size}, compressed={compressed_size}")
                
                # Read the compressed chunk
                compressed_chunk = f_in.read(compressed_size)
                if len(compressed_chunk) < compressed_size:
                    print(f"Warning: Incomplete chunk (expected {compressed_size}, got {len(compressed_chunk)})")
                    break
                
                # Decompress the chunk
                decompressed_chunk = decompress(compressed_chunk, uncompressed_size)
                
                # Write the decompressed chunk to the output file
                f_out.write(decompressed_chunk)
                total_decompressed_size += len(decompressed_chunk)
            
            print(f"Total decompressed size: {total_decompressed_size} bytes")
            return total_decompressed_size

def decompress(input_buffer, output_buffer_size):
    """
    Decompress the input buffer using a variant of the LZ77 algorithm.
    
    Args:
        input_buffer (bytes or bytearray): The compressed input data.
        output_buffer_size (int): The expected size of the decompressed data.
        
    Returns:
        bytearray: The decompressed data.
    """
    if not input_buffer:
        return bytearray()
    
    output_buffer = bytearray(output_buffer_size)
    
    kind_bit = 0  # Current bit position in the Kind value
    have_nibble = False  # Whether we have a pending nibble from a previous read
    output_buffer_index = 0  # Current position in the output buffer
    input_buffer_index = 0  # Current position in the input buffer
    nibble_value = 0  # Value of the pending nibble
    kind = 0  # Current Kind value (flags for whether bytes are literal or sequences)
    
    while output_buffer_index < output_buffer_size:
        # If we've used all bits in Kind, read a new 32-bit Kind value
        if kind_bit == 0:
            if input_buffer_index + 3 >= len(input_buffer):
                break  # Not enough data left to read a new Kind value
            
            kind = (input_buffer[input_buffer_index] | 
                   (input_buffer[input_buffer_index + 1] << 8) | 
                   (input_buffer[input_buffer_index + 2] << 16) | 
                   (input_buffer[input_buffer_index + 3] << 24))
            input_buffer_index += 4
            kind_bit = 32
        
        kind_bit -= 1
        
        # Check the current bit in Kind to determine if we're copying a literal byte or a sequence
        if (kind & (1 << kind_bit)) == 0:
            # Copy a literal byte
            if input_buffer_index >= len(input_buffer):
                break  # Not enough data left to read a literal byte
            
            output_buffer[output_buffer_index] = input_buffer[input_buffer_index]
            input_buffer_index += 1
            output_buffer_index += 1
        else:
            # Copy a sequence
            if input_buffer_index + 1 >= len(input_buffer):
                break  # Not enough data left to read the length_offset
            
            length_offset = input_buffer[input_buffer_index] | (input_buffer[input_buffer_index + 1] << 8)
            input_buffer_index += 2
            
            offset = length_offset >> 3
            length = length_offset & 7
            
            if length == 7:
                if not have_nibble:
                    if input_buffer_index >= len(input_buffer):
                        break  # Not enough data left to read a nibble
                    
                    have_nibble = True
                    nibble_value = input_buffer[input_buffer_index]
                    length = nibble_value & 15
                    input_buffer_index += 1
                else:
                    length = nibble_value >> 4
                    have_nibble = False
                
                if length == 15:
                    if input_buffer_index >= len(input_buffer):
                        break  # Not enough data left to read the extended length
                    
                    length = input_buffer[input_buffer_index]
                    input_buffer_index += 1
                    
                    if length == 255:
                        if input_buffer_index + 1 >= len(input_buffer):
                            break  # Not enough data left to read the 16-bit extended length
                        
                        length = input_buffer[input_buffer_index] | (input_buffer[input_buffer_index + 1] << 8)
                        input_buffer_index += 2
                        length -= 22
                    
                    length += 15
                
                length += 7
            
            length += 3
            
            # Check if offset is valid
            if offset + 1 > output_buffer_index:
                break  # Invalid offset (would read before the start of the output buffer)
            
            # Copy the sequence, handling overlap
            for i in range(length):
                if output_buffer_index >= output_buffer_size:
                    break  # Output buffer is full
                
                output_buffer[output_buffer_index] = output_buffer[output_buffer_index - offset - 1]
                output_buffer_index += 1
    
    return output_buffer


# File-based usage
if __name__ == "__main__":
    import os
    import argparse
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Decompress files using Xpress8 algorithm')
    parser.add_argument('--mode', choices=['single', 'chunked'], default='chunked',
                      help='Decompression mode: single buffer or chunked file format (default: chunked)')
    parser.add_argument('--input', default='data/output/metadata.sqlitedb',
                      help='Input compressed file (default: data/output/metadata.sqlitedb)')
    parser.add_argument('--output', default='out.bin',
                      help='Output decompressed file (default: out.bin)')
    
    args = parser.parse_args()
    
    try:
        if args.mode == 'chunked':
            # Use the chunked decompression format
            print(f"Decompressing chunked file {args.input} to {args.output}...")
            total_size = xpress8_decompress(args.input, args.output)
            print(f"Successfully decompressed {total_size} bytes to {args.output}")
        else:
            # Use the single buffer decompression format
            with open(args.input, 'rb') as f:
                compressed_data = bytearray(f.read())
            
            # Get the size of the file to estimate output size
            # In a real implementation, this size might be stored in a header
            # For now, we'll assume output is 10x larger than input as an estimate
            # You may need to adjust this based on your specific compression ratio
            estimated_output_size = len(compressed_data) * 10
            
            print(f"Read {len(compressed_data)} bytes from {args.input}")
            print(f"Estimated output size: {estimated_output_size} bytes")
            
            # Decompress the data
            result = decompress(compressed_data, estimated_output_size)
            
            # Write decompressed data to output file
            with open(args.output, 'wb') as f:
                f.write(result)
            
            print(f"Successfully decompressed {len(result)} bytes to {args.output}")
    
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found")
    except Exception as e:
        print(f"Error during decompression: {e}")