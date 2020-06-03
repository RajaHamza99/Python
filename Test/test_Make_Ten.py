import pytest
from Code import Make_Ten


def test_Make_Ten():
    assert Make_Ten.makes_ten(10, 10) == True