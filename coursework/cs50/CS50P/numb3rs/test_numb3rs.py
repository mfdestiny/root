from numb3rs import validate


def test_default():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("a.a.a.a") == False
    assert validate("255.267.266.600") == False
    assert validate("cat.") == False
    assert validate("cat.cat") == False
    assert validate("255.255.255") == False
    assert validate("1") == False
    assert validate("1.") == False

if __name__ == "__main__":
    test_default()