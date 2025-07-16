import pytest


def test_lawn_grass(first_lawn_grass):
    assert first_lawn_grass.name == "Газонная трава"
    assert first_lawn_grass.description == "Элитная трава для газона"
    assert first_lawn_grass.price == 500.0
    assert first_lawn_grass.quantity == 20
    assert first_lawn_grass.country == "Россия"
    assert first_lawn_grass.germination_period == "7 дней"
    assert first_lawn_grass.color == "Зеленый"


def test_lawn_grasses_add(first_lawn_grass, second_lawn_grass):
    assert first_lawn_grass + second_lawn_grass == 16750.0


def test_lawn_grasses_add_error(first_lawn_grass):
    with pytest.raises(TypeError):
        raise first_lawn_grass + 21
