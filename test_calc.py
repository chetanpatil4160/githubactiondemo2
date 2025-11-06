import pytest

from calc import add,sub,mul,div

def test_add():
    # in unit test caess we compare actual o/p vs expected o/p
    assert add(2,3) == 5

def test_sub():
    # in unit test caess we compare actual o/p vs expected o/p
    assert sub(3,1) == 2

def test_mul():
    # in unit test caess we compare actual o/p vs expected o/p
    assert mul(4,2) == 8

def test_div():
    # in unit test caess we compare actual o/p vs expected o/p
    assert div(4,2) == 2