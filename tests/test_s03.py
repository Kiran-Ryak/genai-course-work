"""Session 3 checkpoint. Run from the adv-genai folder with:  uv run pytest tests/test_s03.py

The tests read YOUR file: mywork/clean_text.py
"""
import sys
from pathlib import Path

import pytest

MYWORK = Path(__file__).resolve().parent.parent / "mywork"
sys.path.insert(0, str(MYWORK))


@pytest.fixture(scope="module")
def ct():
    if not (MYWORK / "clean_text.py").exists():
        pytest.fail("mywork/clean_text.py not found. Copy starters/s03_clean_text.py "
                    "to mywork/clean_text.py first (README, Session 3, step 2).")
    import clean_text
    return clean_text


def test_normalise_spaces(ct):
    assert ct.normalise_spaces("  Home   loan  status ") == "Home loan status"
    assert ct.normalise_spaces("") == ""


def test_mask_pan_masks_a_pan(ct):
    assert ct.mask_pan("ABCDE1234F") == "XXXXXX234F"


def test_mask_pan_leaves_other_words(ct):
    for word in ["loan", "ABCDE12345", "ABCD1234F", "1234567890"]:
        assert ct.mask_pan(word) == word, f"{word!r} is not a PAN and must not change"


def test_mask_phone_masks_ten_digits(ct):
    assert ct.mask_phone("9876543210") == "XXXXXX3210"


def test_mask_phone_leaves_other_words(ct):
    for word in ["98765", "98765432100", "ABCDE1234F", "status"]:
        assert ct.mask_phone(word) == word, f"{word!r} is not a 10-digit phone number"


def test_unique_lines_keeps_first_and_order(ct):
    lines = ["b", "a", "b", "c", "a"]
    assert ct.unique_lines(lines) == ["b", "a", "c"]
    assert lines == ["b", "a", "b", "c", "a"], "do not change the list you were given"


def test_word_counts(ct):
    assert ct.word_counts("Loan status loan") == {"loan": 2, "status": 1}
    assert ct.word_counts("") == {}


def test_mask_message(ct):
    text = "  My PAN is ABCDE1234F   and phone 9876543210 "
    assert ct.mask_message(text) == "My PAN is XXXXXX234F and phone XXXXXX3210"
