import numpy as np

_CHR_TABLE = [chr(i) for i in range(256)]


def decompress_encode_array(compressed):
    arr = np.frombuffer(bytes(compressed), dtype=np.uint8)
    full_array = np.empty(256, dtype=np.int64)
    full_array[0::2] = arr & 0x0F
    full_array[1::2] = (arr >> 4) & 0x0F
    return full_array.tolist()


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
        codes[character] = (code, length)
        code += 1
    return codes


def build_huffman_table(encode_array):
    codes = generate_codes(encode_array)
    max_len = max(length for _, length in codes.values()) if codes else 0
    if max_len == 0:
        return [], 0
    table_size = 1 << max_len
    table = [None] * table_size
    for symbol, (code_val, code_len) in codes.items():
        padding_bits = max_len - code_len
        for suffix in range(1 << padding_bits):
            idx = (code_val << padding_bits) | suffix
            table[idx] = (symbol, code_len)
    return table, max_len


def _swap_bitstream(bitstream):
    raw = bytes(bitstream)
    n = len(raw)
    arr = np.frombuffer(raw, dtype=np.uint8)
    result = np.empty(n, dtype=np.uint8)
    even = n & ~1
    if even > 0:
        pairs = arr[:even].reshape(-1, 2)
        swapped = pairs[:, ::-1].reshape(-1)
        result[:even] = swapped
    if n & 1:
        result[-1] = arr[-1]
    return bytes(result)


def decode_substrings(swapped, table, max_len, offsets, store_total_bits):
    table_mask = (1 << max_len) - 1
    chr_table = _CHR_TABLE
    n_strings = len(offsets)
    results = [None] * n_strings
    swapped_bytes = swapped

    for s in range(n_strings):
        start_bit = offsets[s]
        end_bit = offsets[s + 1] if s + 1 < n_strings else store_total_bits
        chars = []
        bit_pos = start_bit

        while bit_pos < end_bit:
            byte_pos = bit_pos >> 3
            bit_offset = bit_pos & 7
            needed_bytes = (bit_offset + max_len + 7) >> 3

            val = int.from_bytes(swapped_bytes[byte_pos:byte_pos + needed_bytes], 'big')
            val >>= (needed_bytes * 8 - bit_offset - max_len)
            val &= table_mask

            symbol, code_len = table[val]
            chars.append(chr_table[symbol])
            bit_pos += code_len

        results[s] = ''.join(chars)

    return results


def decode_substring(swapped, table, max_len, start_bit, end_bit):
    table_mask = (1 << max_len) - 1
    chr_table = _CHR_TABLE
    result = []
    bit_pos = start_bit

    while bit_pos < end_bit:
        byte_pos = bit_pos >> 3
        bit_offset = bit_pos & 7
        needed_bytes = (bit_offset + max_len + 7) >> 3

        val = int.from_bytes(swapped[byte_pos:byte_pos + needed_bytes], 'big')
        val >>= (needed_bytes * 8 - bit_offset - max_len)
        val &= table_mask

        symbol, code_len = table[val]
        result.append(chr_table[symbol])
        bit_pos += code_len

    return ''.join(result)
