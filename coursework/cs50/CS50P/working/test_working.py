from working import convert
import pytest

def test_default():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

