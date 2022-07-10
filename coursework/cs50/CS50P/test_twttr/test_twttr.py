from twttr import shorten

def test_default():
    assert shorten("twitter") == "twttr"

def test_2vowels():
    assert shorten("you") == "y"

def test_Vowel():
    assert shorten("Twitter") == "Twttr"
    assert shorten("twiTTer") == "twTTr"

def test_numbers():
    assert shorten("apple123") == "ppl123"

def test_punc():
    assert shorten(".apple") == ".ppl"

def test_cap():
    assert shorten("twittEr") == "twttr"