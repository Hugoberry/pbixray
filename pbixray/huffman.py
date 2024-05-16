class HuffmanTree:
    def __init__(self, c=0):
        self.c = c
        self.left = None
        self.right = None

# Helper function to convert ISO-8859-1 code to UTF-8 string
def iso88591_to_utf8(code):
    if code >= 0x80:
        return bytes([0xC2 + (code > 0xBF), (code & 0x3F) + 0x80]).decode('utf-8')
    else:
        return chr(code)

# Function to generate the full 256-byte Huffman array from the compact 128-byte encode_array
def decompress_encode_array(compressed):
    full_array = [0] * 256
    for i, byte in enumerate(compressed):
        full_array[2 * i] = byte & 0x0F         # Lower nibble
        full_array[2 * i + 1] = (byte >> 4) & 0x0F  # Upper nibble
    return full_array

# Function to generate Huffman codes based on codeword lengths
def generate_codes(lengths):
    codes = {}
    sorted_lengths = [(lengths[i], i) for i in range(256) if lengths[i] != 0]
    sorted_lengths.sort()

    code = 0
    last_length = 0
    for length, character in sorted_lengths:
        if last_length != length:
            code <<= (length - last_length)
            last_length = length
        codes[character] = bin(code)[2:].zfill(length)
        code += 1
    return codes

# Function to build Huffman tree based on generated codes
def build_huffman_tree(encode_array):
    codes = generate_codes(encode_array)
    root = HuffmanTree()
    for character, code in codes.items():
        node = root
        for bit in code:
            if bit == '0':
                if not node.left:
                    node.left = HuffmanTree()
                node = node.left
            else:
                if not node.right:
                    node.right = HuffmanTree()
                node = node.right
        node.c = character
    return root

# Function to decode a bitstream from start to end bit positions using the Huffman tree
def decode_substring(bitstream, tree, start_bit, end_bit):
    result = ""
    node = tree
    total_bits = end_bit - start_bit
    for i in range(total_bits):
        bit_pos = start_bit + i
        byte_pos = bit_pos // 8
        bit_offset = bit_pos % 8
        byte_pos = (byte_pos & ~0x01) + (1 - (byte_pos & 0x01))

        if not node.left and not node.right:
            result += iso88591_to_utf8(node.c)
            node = tree

        if bitstream[byte_pos] & (1 << (7 - bit_offset)):
            node = node.right
        else:
            node = node.left

    if not node.left and not node.right:
        result += iso88591_to_utf8(node.c)

    return result
