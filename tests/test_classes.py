from src.classes import Category, Product


def test_products(first_product, second_product):
    assert first_product.name == "Ipone"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 25000.12
    assert first_product.quantity == 5
    assert second_product.name == "Samsung"
    assert second_product.description == "128GB, Белый цвет"
    assert second_product.price == 12000.12
    assert second_product.quantity == 2


def test_category(first_category):
    assert first_category.name == "Телефоны"
    assert first_category.description == "Хорошие телефоны"
    assert len(first_category.products) == 2
    assert first_category.category_count == 1
    assert first_category.product_count == 2


def test_product_update(capsys, first_product):
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_create():
    test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    test_product.name = "Iphone 15"
    test_product.description = "512GB, Gray space"
    test_product.price = 210000.0
    test_product.quantity = 8


def test_new_product_creation():
    product_data = {"name": "Ноутбук", "description": "16GB RAM, 1TB SSD", "price": 90000, "quantity": 3}
    product = Product.new_product(product_data)

    assert product.name == product_data["name"]
    assert product.description == product_data["description"]
    assert product.price == product_data["price"]
    assert product.quantity == product_data["quantity"]


def test_category_add_product(first_category, first_product):
    initial_count = len(first_category.products)
    initial_total = Category.product_count

    first_category.add_product(first_product)

    assert len(first_category.products) == initial_count + 1
    assert Category.product_count == initial_total + 1
    assert first_category.products[-1].name == "Ipone"

def test_product_print(first_product, second_product):
    assert str(first_product) == "Ipone, 25000.12 руб. Остаток: 5 шт."
    assert str(second_product) == "Samsung, 12000.12 руб. Остаток: 2 шт."

def test_products_sum(first_product, second_product):
    assert first_product + second_product == 149000.84

def test_category_print(first_category):
    assert str(first_category) == "Телефоны, количество продуктов: 6 шт."