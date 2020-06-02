pip3 install pytest

import pytest 

def func(num):
    return num * 2

def test_answer():
    assert func(6) == 10
