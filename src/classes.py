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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

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
            print("Цена не должна быть нулевая или отрицательная")
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

    def __str__(self):
        all_products = 0
        for product in self.__products:
            all_products += product.quantity
        return f"{self.name}, количество продуктов: {all_products} шт."

    @property
    def products_srt(self) -> None:
        products_str = ""
        for output_product in self.__products:
            products_str += (
                f"{str(output_product)} шт.\n"
            )
        return products_str

    @property
    def products(self):
        return self.__products

    def add_product(self, adding_product: Product):
        presence: bool = False
        for output in self.__products:
            if adding_product.name == output.name:
                output.price = adding_product.price
                output.quantity = output.quantity + adding_product.quantity
                presence = True
        if not presence:
            self.__products.append(adding_product)
            Category.product_count += 1
