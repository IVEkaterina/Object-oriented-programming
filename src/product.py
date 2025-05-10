class Product:
    """Класс для продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """ Конструктор для продукта """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Строковое отображение класса Product """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Сложение всей стоимости товаров(цена*кол-во) """
        return (self.__price*self.quantity) + (other.__price*other.quantity)

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
