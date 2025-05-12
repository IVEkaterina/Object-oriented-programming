from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстратный класкс для продукта """

    @abstractmethod
    def __str__(self):
        """ Метод для строкового отображения """
        pass

    @abstractmethod
    def __init__(self):
        """ Конструктор для продукта """
        pass

    @abstractmethod
    def __add__(self, other):
        """ Метод для сложения стоимости товаров """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product: dict):
        """ Класс-метод для создания нового продукта """
        pass

    @property
    @abstractmethod
    def price(self):
        """ Метод, возвращающий цену """
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float):
        """ Метод для проверки цены """
        pass


class MixinPrint:
    def __init__(self, *args, **kwargs):
        print(f'{self.__class__.__name__}{args}')


class Product(MixinPrint, BaseProduct):
    """ Класс для продукта """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """ Конструктор для продукта """
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Строковое отображение класса Product """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Сложение всей стоимости товаров(цена*кол-во) """
        if not isinstance(other, type(self)):
            raise TypeError
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product: dict):
        """ Класс-метод, возвращающий созданный объект класса Product """
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Метод, возвращающий цену """
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Метод для проверки положительности цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    """ Класс для смартфонов """
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        """ Конструктор для смартфонов """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Класс для газонной травы"""
    country: str
    germination_period: str
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        """ Конструктор для газонной травы """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
