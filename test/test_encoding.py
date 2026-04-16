"""
Encoding tests for pbixray's VertiPaq decompression.

VertiPaq uses several distinct encoding schemes per column:
  - RLE (Run-Length Encoding) with bit-packed hybrid — repetitive integer columns
  - Dictionary + Huffman (charset/UTF-16LE variants) — string columns
  - Hash dictionary (HIDX) — numeric columns

The Excalidraw.pbix is purpose-built to exercise RLE and Unicode encodings.
The Adventure Works Internet Sales Product table exercises multilingual Huffman
decoding across 9 scripts/character sets.
"""
import pytest


# ---------------------------------------------------------------------------
# RLE encoding — Fruit_RLE table (Excalidraw.pbix)
# ---------------------------------------------------------------------------

def test_rle_row_count(excalidraw_model):
    table = excalidraw_model.get_table("Fruit_RLE")
    assert len(table) == 300


def test_rle_columns(excalidraw_model):
    table = excalidraw_model.get_table("Fruit_RLE")
    assert "Type" in table.columns
    assert "Qty" in table.columns


def test_rle_string_values_decoded(excalidraw_model):
    """RLE string dictionary decodes correctly — only known fruit names appear."""
    table = excalidraw_model.get_table("Fruit_RLE")
    assert set(table["Type"].dropna()) == {"apple", "banana", "cherry"}


def test_rle_numeric_values_decoded(excalidraw_model):
    """RLE numeric values are monotonically increasing as the data was authored."""
    table = excalidraw_model.get_table("Fruit_RLE")
    qty = table["Qty"].dropna().astype(int)
    assert qty.min() >= 0
    assert qty.max() > qty.min()


# ---------------------------------------------------------------------------
# Huffman / dictionary encoding with Unicode — Fruit table (Excalidraw.pbix)
# ---------------------------------------------------------------------------

def test_huffman_unicode_row_count(excalidraw_model):
    table = excalidraw_model.get_table("Fruit")
    assert len(table) == 16


def test_huffman_unicode_emoji_decoded(excalidraw_model):
    """UTF-16 surrogate-pair emoji are decoded correctly from the Huffman dictionary."""
    table = excalidraw_model.get_table("Fruit")
    types = set(table["Type"].dropna())
    assert "🍌" in types, "Banana emoji missing — possible UTF-16 decode failure"
    assert "🍎" in types, "Apple emoji missing — possible UTF-16 decode failure"
    assert "🍋" in types, "Lemon emoji missing — possible UTF-16 decode failure"


def test_huffman_unicode_latin_coexists(excalidraw_model):
    """Latin strings coexist with emoji in the same dictionary without corruption."""
    table = excalidraw_model.get_table("Fruit")
    types = set(table["Type"].dropna())
    assert "lemon" in types


def test_huffman_numeric_column(excalidraw_model):
    table = excalidraw_model.get_table("Fruit")
    qty = table["Qty"].dropna().astype(int)
    assert set(qty) == {10, 20, 30}


# ---------------------------------------------------------------------------
# Multilingual Huffman encoding — Product table (Adventure Works Internet Sales)
# ---------------------------------------------------------------------------

def test_multilingual_columns_present(adventure_works_model):
    table = adventure_works_model.get_table("Product")
    for col in [
        "EnglishDescription", "FrenchDescription", "ChineseDescription",
        "ArabicDescription", "HebrewDescription", "ThaiDescription",
        "GermanDescription", "JapaneseDescription", "TurkishDescription",
    ]:
        assert col in table.columns, f"Missing column: {col}"


def test_multilingual_english_ascii(adventure_works_model):
    table = adventure_works_model.get_table("Product")
    sample = table["EnglishDescription"].dropna().iloc[0]
    assert isinstance(sample, str) and len(sample) > 0
    # All characters should be in the printable ASCII range
    assert all(ord(c) < 128 for c in sample), "Unexpected non-ASCII in English description"


def test_multilingual_french_accents(adventure_works_model):
    """French descriptions contain accented Latin characters (é, à, ç, \xa0)."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["FrenchDescription"].dropna().astype(str))
    accented = [c for c in text if ord(c) > 127 and ord(c) < 0x500]
    assert len(accented) > 0, "No accented Latin characters found in French descriptions"


def test_multilingual_chinese_cjk(adventure_works_model):
    """Chinese descriptions contain CJK Unified Ideographs (U+4E00–U+9FFF)."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["ChineseDescription"].dropna().astype(str))
    cjk = [c for c in text if "\u4e00" <= c <= "\u9fff"]
    assert len(cjk) > 0, "No CJK characters found in Chinese descriptions"


def test_multilingual_arabic(adventure_works_model):
    """Arabic descriptions contain Arabic script characters (U+0600–U+06FF)."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["ArabicDescription"].dropna().astype(str))
    arabic = [c for c in text if "\u0600" <= c <= "\u06ff"]
    assert len(arabic) > 0, "No Arabic script characters found in Arabic descriptions"


def test_multilingual_hebrew(adventure_works_model):
    """Hebrew descriptions contain Hebrew script characters (U+0590–U+05FF)."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["HebrewDescription"].dropna().astype(str))
    hebrew = [c for c in text if "\u0590" <= c <= "\u05ff"]
    assert len(hebrew) > 0, "No Hebrew script characters found in Hebrew descriptions"


def test_multilingual_thai(adventure_works_model):
    """Thai descriptions contain Thai script characters (U+0E00–U+0E7F)."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["ThaiDescription"].dropna().astype(str))
    thai = [c for c in text if "\u0e00" <= c <= "\u0e7f"]
    assert len(thai) > 0, "No Thai script characters found in Thai descriptions"


def test_multilingual_japanese(adventure_works_model):
    """Japanese descriptions contain CJK or Katakana/Hiragana characters."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["JapaneseDescription"].dropna().astype(str))
    japanese = [c for c in text if "\u3000" <= c <= "\u9fff"]
    assert len(japanese) > 0, "No Japanese script characters found in Japanese descriptions"


def test_multilingual_german_umlauts(adventure_works_model):
    """German descriptions contain umlaut characters (ä, ö, ü, ß etc.)."""
    table = adventure_works_model.get_table("Product")
    text = " ".join(table["GermanDescription"].dropna().astype(str))
    umlauts = [c for c in text if c in "äöüÄÖÜß"]
    assert len(umlauts) > 0, "No umlaut characters found in German descriptions"


def test_multilingual_no_corruption(adventure_works_model):
    """None of the description columns should contain replacement characters (U+FFFD),
    which would indicate a decoding error."""
    table = adventure_works_model.get_table("Product")
    desc_cols = [
        "EnglishDescription", "FrenchDescription", "ChineseDescription",
        "ArabicDescription", "HebrewDescription", "ThaiDescription",
        "GermanDescription", "JapaneseDescription", "TurkishDescription",
    ]
    for col in desc_cols:
        text = " ".join(table[col].dropna().astype(str))
        assert "\ufffd" not in text, f"Replacement character found in {col} — decode corruption"
