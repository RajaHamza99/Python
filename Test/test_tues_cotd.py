import pytest
from Code.tues_cotd import split

test = "hello,world,without,comma"

def test_tues_cotd():
    assert split(test) == ["comma", "hello", "without", "world"]