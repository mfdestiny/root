import project
from journal import Journal as journal
import pytest

def test_default():
    assert project.parse_input("hello") == ('hello',None)
    assert project.parse_input("read 2") == ('read',2)

def test_journal():
    j = journal()
    assert j.size == 0

def test_exceptions():
    with pytest.raises(TypeError):
        project.parse_input('read a')

def test_read():
    with pytest.raises(ValueError):
        project.read(0)

def test_journal_entry():
    with pytest.raises(ValueError):
        j = journal()
        j.get_entry(0)

def test_journal_last():
    j = journal()
    assert j.last_entry() == None