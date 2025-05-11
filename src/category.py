from src.product import Product


class Category:
    """Класс для категории"""
    name: str
    description: str
    products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """ Конструктор для категорий """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """ Строковое отображение класса Category """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: list) -> None:
        """ Метод для добавления товаров в категорию """
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты класса Product или его наследников.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """ Метод который выводит список товаров в виде строк в формате:
        'Название продукта, X руб. Остаток: X шт.\n'"""
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_list(self) -> list:
        """ Метод, возвращающий список продуктов """
        return self.__products
