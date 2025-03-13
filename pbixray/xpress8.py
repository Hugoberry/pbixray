class Xpress8:
    """
    Class for decompressing data using the Xpress8 compression algorithm.
    Provides methods for single buffer decompression and chunked data decompression.
    """
    
    @staticmethod
    def decompress(input_buffer, output_buffer_size):
        """
        Decompress a single compressed buffer using the Xpress8 algorithm.
        
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

    @staticmethod
    def decompress_chunked(input_buffer):
        """
        Decompress a buffer containing multiple compressed chunks.
        Each chunk starts with a 4-byte header:
        - First 2 bytes (uint16): Size of the uncompressed chunk
        - Next 2 bytes (uint16): Size of the compressed chunk
        
        Args:
            input_buffer (bytes or bytearray): The compressed input data with chunk headers
            
        Returns:
            bytearray: The fully decompressed data from all chunks
        """
        if not input_buffer:
            return bytearray()
        
        output_buffer = bytearray()
        input_buffer_index = 0
        
        # Process all chunks until end of buffer
        while input_buffer_index < len(input_buffer):
            # Ensure we have enough data for the chunk header (4 bytes)
            if input_buffer_index + 4 > len(input_buffer):
                break
            
            # Extract uncompressed and compressed sizes from header (little-endian 2-byte integers)
            uncompressed_size = input_buffer[input_buffer_index] | (input_buffer[input_buffer_index + 1] << 8)
            input_buffer_index += 2
            
            compressed_size = input_buffer[input_buffer_index] | (input_buffer[input_buffer_index + 1] << 8)
            input_buffer_index += 2
            
            # Check if we have enough data for the compressed chunk
            if input_buffer_index + compressed_size > len(input_buffer):
                break
            
            # Extract the compressed chunk
            compressed_chunk = input_buffer[input_buffer_index:input_buffer_index + compressed_size]
            input_buffer_index += compressed_size
            
            # Decompress the chunk and append to the output buffer
            decompressed_chunk = Xpress8.decompress(compressed_chunk, uncompressed_size)
            output_buffer.extend(decompressed_chunk)
        
        return output_buffer