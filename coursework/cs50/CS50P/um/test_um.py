from um import count


def test_default():
    assert count("um") == 1
    assert count("album") == 0
    assert count("Um") == 1