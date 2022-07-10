from fuel import convert
from fuel import gauge
import pytest

def test_default():
    assert convert("2/3") == 67
    assert convert("3/3") == 100
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"

def test_ValError():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_ZError():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")