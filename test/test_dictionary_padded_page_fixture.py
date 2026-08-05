"""Engine-authored regression fixture for the padded uncompressed dictionary page.

``data/padded-dictionary-page.dictionary`` is one real ``.dictionary`` stream,
lifted byte-for-byte out of a VertiPaq model (2,171,367 bytes). Only the
dictionary is committed -- it is the whole input to ``_read_dictionary``, so no
surrounding model is needed to exercise the decode, and the file still parses
directly with ``docs/dictionary.ksy``. It holds the ``City`` column of a
Geography dimension, values of the form ``Stephens City, VA, USA``.

Shape:

    page 0  uncompressed  28,419 strings  used=524,281 chars
                          allocation=1,048,576 bytes  remaining=7
    page 1  Huffman       40,492 strings  page_start_index=28,419
    page 2  Huffman       21,483 strings  page_start_index=68,911

The 1 MiB allocation holds seven characters of NUL slack past the last string.
Splitting the whole allocation on NUL therefore yields 28,426 entries for a
page the engine says holds 28,419, and every id on the two Huffman pages --
which is where 62% of the column's rows point -- lands seven too high.

Padded pages are rare: across 596 local models (17,249 string dictionaries,
15,185 uncompressed pages) only 58 pages carry padding, which is why this went
unnoticed. A dictionary has to spill past the 1 MiB page to produce one.

Nothing here hardcodes what the decoder produced. The anchors are the engine's
own numbers: each page's ``page_start_index`` -- the base data id the engine
assigned -- and the column's declared cardinality of 90,394, which the page
counts must also add up to.

On 90,394 vs 90,395: DAX Studio reports 90,395 for this column because it
counts BLANK as a distinct value, and 1,625 of the source table's rows decode
to null (their data ids sit below the dictionary's base id, so they never reach
the dictionary). ``PBIXRay.statistics.Cardinality`` and the stored dictionary
both say 90,394 -- stored values only, which does include a real empty string
of the column's own. Do not "correct" the constant below to match DAX Studio.
"""
import io
import os

import pytest

from pbixray.column_data.dictionary import ColumnDataDictionary
from pbixray.vertipaq_decoder import VertiPaqDecoder

FIXTURE = os.path.join(os.path.dirname(__file__), '..', 'data',
                       'padded-dictionary-page.dictionary')

DECLARED_CARDINALITY = 90394
FIRST_DATA_ID = 3


@pytest.fixture(scope="module")
def dictionary_buffer():
    with open(FIXTURE, "rb") as f:
        return f.read()


@pytest.fixture(scope="module")
def pages(dictionary_buffer):
    with io.BytesIO(dictionary_buffer) as f:
        return ColumnDataDictionary.from_io(f).data.dictionary_pages


@pytest.fixture(scope="module")
def decoded(dictionary_buffer):
    decoder = VertiPaqDecoder.__new__(VertiPaqDecoder)  # no model needed
    return decoder._read_dictionary(dictionary_buffer, min_data_id=FIRST_DATA_ID)


def test_first_page_carries_padding(pages):
    """The fixture is only meaningful while its first page is still padded."""
    store = pages[0].string_store
    assert pages[0].page_compressed == 0
    assert store.remaining_store_available == 7
    assert store.buffer_used_characters == 524281
    assert store.allocation_size == 1048576
    assert [p.page_compressed for p in pages] == [0, 1, 1]


def test_entry_count_matches_declared_cardinality(decoded):
    """One entry per distinct value -- no phantom entries from the padding."""
    assert decoded.is_string
    assert len(decoded.values) == DECLARED_CARDINALITY
    assert max(decoded.values) == FIRST_DATA_ID + DECLARED_CARDINALITY - 1


def test_pages_start_where_the_engine_says(pages, decoded):
    """Every page's ids must begin at its own ``page_start_index``.

    This is the failure the padding causes: the phantom entries push the base
    index of each following page out by ``remaining_store_available``, so the
    column silently returns a neighbouring row's value.
    """
    running = 0
    for page in pages:
        assert page.page_start_index == running
        # A real value sits on each page's first id -- under the bug the first
        # ids of pages 1 and 2 hold the padding's empty strings instead.
        assert decoded.values[FIRST_DATA_ID + page.page_start_index]
        running += page.page_string_count
    assert running == DECLARED_CARDINALITY
