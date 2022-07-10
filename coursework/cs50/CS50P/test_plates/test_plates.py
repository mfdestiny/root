from plates import is_valid as validate

def test_default():
    assert validate("AAA") == True

def test_alpha():
    assert validate("CS50") == True

def test_over():
    assert validate("AAAAAAAA") == False

def test_frontNumber():
    assert validate("11111") == False

def test_numberMiddle():
    assert validate("AA2AA") == False

def test_numberEnd():
    assert validate("AA222") == True

def test_zeroBegin():
    assert validate("CS05") == False

def test_punc():
    assert validate("PI3.14") == False

def test_length():
    assert validate("A") == False