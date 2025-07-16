import pytest

from src.classes import Category, Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def first_product():
    return Product(name="Ipone", description="256GB, Серый цвет, 200MP камера", price=25000.12, quantity=5)


@pytest.fixture
def second_product():
    return Product(name="Samsung", description="128GB, Белый цвет", price=12000.12, quantity=2)


@pytest.fixture
def first_category():
    return Category(
        name="Телефоны",
        description="Хорошие телефоны",
        products=[
            Product("Xiaomi", "64GB", 125, 2),
            Product("Samsung", "64GB", 255, 4),
        ],
    )

@pytest.fixture
def first_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

@pytest.fixture
def first_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

@pytest.fixture
def second_lawn_grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
