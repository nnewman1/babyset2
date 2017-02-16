# Nicholas Newman

# test_babyset.py
# Demonstrates unit testing using the pytest module.
# pytest must be installed through pip.

import pytest

from baby_set import BabySet

def test_init():
    bset = BabySet([2, 4, 4])
    assert bset.size() == 2

def test_init_empty():
    bset = BabySet()
    assert bset.size() == 0

def test_add():
    bset = BabySet([2, 4, 4])
    bset.add(4)
    assert bset.size() == 2

def test_addSeq():
    bset = BabySet([2,4,4])
    bset.addSeq([2,4,5,6])
    assert bset.size() == 4

def test_get():
    bset = BabySet([2,4,4])
    bset.get(4)
    assert bset.size() == 2

def test_remove():
    bset = BabySet([2,4,4])
    bset.remove(2)
    assert bset.size() == 1

def test_clear():
    bset = BabySet([2,4,4])
    bset.clear()
    assert bset.size() == 0

if __name__ == '__main__':
    pytest.main()


