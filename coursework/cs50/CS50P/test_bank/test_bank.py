from bank import value

def test_default():
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("zip") == 100

def test_numbers():
    assert value("123") == 100

def test_Cap():
    assert value("Zip") == 100

def test_punc():
    assert value("hey!") == 20