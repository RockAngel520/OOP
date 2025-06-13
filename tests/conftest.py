import pytest

from src.classes import Product, Category

@pytest.fixture
def first_product():
    return Product(
        name="Ipone",
        description="256GB, Серый цвет, 200MP камера",
        price=25000.12,
        quantity=5
    )

@pytest.fixture
def second_product():
    return Product(
        name="Samsung",
        description="128GB, Белый цвет",
        price=12000.12,
        quantity=2
    )

@pytest.fixture
def first_category():
    return Category(
        name="Телефоны",
        description="Хорошие телефоны",
        products=[
            Product("Xiaomi", "64GB", 125, 2),
            Product("Samsung", "64GB", 255, 4),
        ]
    )

