import pytest


def test_smartphone(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_smartphones_add(first_smartphone, second_smartphone):
    assert first_smartphone + second_smartphone == 2580000.0


def test_smartphones_add_error(first_smartphone):
    with pytest.raises(TypeError):
        raise first_smartphone + 21
