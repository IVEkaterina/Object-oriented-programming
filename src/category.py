from src.product import Product


class Category:
    """Класс для категории"""
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, products):
        self.__products.append(products)
        Category.product_count += 1
