"""Uncompressed dictionary pages must not decode their NUL padding as entries.

A string dictionary is a list of pages, and an uncompressed page keeps its
characters in a fixed allocation of which only ``buffer_used_characters`` are
real; the tail is NUL slack. ``_extract_strings`` turns the buffer into entries
by splitting on NUL, so decoding the whole allocation contributes one empty
entry per unused character. ``_read_dictionary`` assigns data ids by walking
pages in order and incrementing, so those phantom entries push the base index
of every *later* page out by ``remaining_store_available``.

Nothing raises when that happens. The shifted ids stay inside the dictionary,
so the column simply returns another row's value -- and the pages that follow
the uncompressed one are the Huffman-compressed ones, i.e. exactly where the
long free-text values live.

None of the sample models carry a padded page (2,246 uncompressed pages across
the 27 readable samples, all of them exactly full), which is why this went
unnoticed; a model large enough to spill a column's dictionary across pages is
needed to produce one. The fixture is therefore synthetic: a two-page string
dictionary built to the on-disk layout, with slack on the first page.

The invariant the fix rests on -- ``allocation_size`` counts bytes while the
two counters above it count UTF-16 characters, so

    allocation_size == 2 * (buffer_used_characters + remaining_store_available)

-- was verified to hold for all 2,246 sample pages plus 1,756 pages of two
~650 MB models that do have padding.
"""
import io
import struct

import pytest

from pbixray.column_data.dictionary import ColumnDataDictionary
from pbixray.vertipaq_decoder import VertiPaqDecoder

PAGE_BEGIN = b"\xDD\xCC\xBB\xAA"
PAGE_END = b"\xCD\xAB\xCD\xAB"


def _uncompressed_page(strings, slack_chars, start_index):
    """One uncompressed string page carrying `slack_chars` NULs of padding."""
    used = "".join(s + "\0" for s in strings)
    used_chars = len(used)
    alloc = 2 * (used_chars + slack_chars)
    return b"".join([
        struct.pack("<Q", 0),                       # page_mask
        struct.pack("<B", 0),                       # page_contains_nulls
        struct.pack("<Q", start_index),             # page_start_index
        struct.pack("<Q", len(strings)),            # page_string_count
        struct.pack("<B", 0),                       # page_compressed
        PAGE_BEGIN,
        struct.pack("<Q", slack_chars),             # remaining_store_available
        struct.pack("<Q", used_chars),              # buffer_used_characters
        struct.pack("<Q", alloc),                   # allocation_size
        used.encode("utf-16-le") + b"\0" * (2 * slack_chars),
        PAGE_END,
    ])


def _string_dictionary(pages_strings, slack_chars):
    """A complete xm_type_string dictionary buffer; slack goes on page 0."""
    total = sum(len(p) for p in pages_strings)
    out = [
        struct.pack("<i", 2),                       # dictionary_type: xm_type_string
        struct.pack("<6i", 0, 8, 64, 6, -1, -1),    # hash_information
        struct.pack("<q", total),                   # store_string_count
        struct.pack("<b", 0),                       # f_store_compressed
        struct.pack("<q", max(len(s) for p in pages_strings for s in p)),
        struct.pack("<q", len(pages_strings)),      # store_page_count
    ]
    start = 0
    for page_id, strings in enumerate(pages_strings):
        out.append(_uncompressed_page(strings, slack_chars if page_id == 0 else 0, start))
        start += len(strings)

    out.append(struct.pack("<Q", total))            # record handle count
    out.append(b"\x08\x00\x00\x00")                 # element_size
    for page_id, strings in enumerate(pages_strings):
        for i in range(len(strings)):
            out.append(struct.pack("<II", i, page_id))
    return b"".join(out)


PAGE0 = ["alpha", "bravo", "charlie"]
PAGE1 = ["delta", "echo"]


@pytest.mark.parametrize("slack_chars", [0, 1, 873])
def test_padding_is_not_decoded_as_entries(slack_chars):
    """Data ids stay put no matter how much slack the first page carries."""
    buffer = _string_dictionary([PAGE0, PAGE1], slack_chars)
    decoder = VertiPaqDecoder.__new__(VertiPaqDecoder)   # no model needed
    decoded = decoder._read_dictionary(buffer, min_data_id=3)

    assert decoded.is_string
    assert decoded.values == dict(enumerate(PAGE0 + PAGE1, start=3))


def test_padding_is_read_but_kept_out_of_the_buffer():
    """The page is still consumed whole -- the end marker has to line up."""
    buffer = _string_dictionary([PAGE0, PAGE1], slack_chars=873)
    with io.BytesIO(buffer) as f:
        parsed = ColumnDataDictionary.from_io(f)

    store = parsed.data.dictionary_pages[0].string_store
    assert store.remaining_store_available == 873
    assert len(store.unused_store_padding) == 2 * 873
    assert store.allocation_size == 2 * (store.buffer_used_characters
                                         + store.remaining_store_available)
    assert store.uncompressed_character_buffer == "alpha\0bravo\0charlie\0"


def test_sample_pages_are_unaffected(work_model):
    """Sanity check on real data: unpadded pages decode as they always did."""
    df = work_model.get_table("Currency")
    assert len(df) == 105
    assert df.loc[df["Code"] == "EUR", "Currency"].iloc[0] == "Euro"
