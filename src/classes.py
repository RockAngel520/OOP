class Product:
    """Класс товаров"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, parameters_list: dict):
        product = Product
        product.name = parameters_list["name"]
        product.description = parameters_list["description"]
        product.price = parameters_list["price"]
        product.quantity = parameters_list["quantity"]
        return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть 0 или меньше нуля")
            return
        elif new_price < self.__price:
            user_input = input("Новая цена ниже. Заменить цену?(Y): ")
            if user_input == "Y" or user_input == "y" or user_input == "Н" or user_input == "н":
                self.__price = new_price
            else:
                return
        self.__price = new_price


class Category:
    """Класс категорий товаров"""

    name: str
    description: str
    __products: list
    category_count: int
    product_count: int

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self) -> None:
        products_str = ''
        for output_product in self.__products:
            products_str += (f'{output_product.name}, {output_product.price} руб. Остаток:'
                             f' {output_product.quantity} шт.\n')
        return products_str

    @property
    def products(self):
        return self.__products

    def add_product(self, adding_product: Product):
        self.__products.append(adding_product)
        Category.product_count += 1
