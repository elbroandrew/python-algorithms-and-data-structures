import pytest
from property_example import Accum


@pytest.fixture
def accum():
    return Accum()


def test_accum_init(accum):
    assert accum.count == 0


def test_accum_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accum_add_three(accum):
    accum.add(3)
    assert accum.count == 3