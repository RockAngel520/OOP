
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
