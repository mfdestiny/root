from jar import Jar


def test_init():
    jar = Jar()
    assert jar != None


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    j = Jar()
    j.deposit(1)
    assert str(j) == "🍪"


def test_withdraw():
    j = Jar()
    j.deposit(1)
    j.withdraw(1)
    assert str(j) == ""
