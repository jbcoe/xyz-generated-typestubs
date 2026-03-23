from xyz_generated_typestubs import add as xyz_add
import pytest


def test_add():
    assert xyz_add(1, 2) == 3


def test_add_negative():
    assert xyz_add(-1, -2) == -3


def test_add_zero():
    assert xyz_add(0, 0) == 0


def test_add_mixed():
    assert xyz_add(1, -1) == 0


def test_add_type_error():
    with pytest.raises(TypeError):
        xyz_add("a", "b")
