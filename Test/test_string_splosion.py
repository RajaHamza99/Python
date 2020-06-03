import pytest
from Code.string_splosion import string_splosion

test = "test"

def test_splosion():
    assert string_splosion(test) == "ttetestest"