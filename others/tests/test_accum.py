import pytest
from property_example import Accum


@pytest.fixture
def accum():
    return Accum()


def test_accum_init(accum):
    accum = Accum()
    assert accum.count == 0


def test_accum_add_one():
    accum = Accum()
    accum.add()
    assert accum.count == 1

def test_accum_add_three():
    accum = Accum()
    accum.add(3)
    assert accum.count == 3