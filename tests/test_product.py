import pytest

from src.product import LawnGrass, Product, Smartphone


@pytest.fixture()
def product_apple():
    return Product("Яблоки", "Яблоки новый урожай", 123.09, 8)


def test_init(product_apple):
    assert product_apple.name == "Яблоки"
    assert product_apple.description == "Яблоки новый урожай"
    assert product_apple.price == 123.09
    assert product_apple.quantity == 8


def test_str_product(product_apple):
    assert str(product_apple) == "Яблоки, 123.09 руб. Остаток: 8 шт."


def test_add_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    assert (product1 + product2) == 2580000.0
    assert (product3 + product2) == 2114000.0
    assert (product1 + product3) == 1334000.0


def test_new_product_from_dict():
    data = {
        "name": "Яйца",
        "description": "Куриные",
        "price": 70.0,
        "quantity": 10
    }

    product = Product.new_product(data)

    assert product.name == "Яйца"
    assert product.description == "Куриные"
    assert product.price == 70.0
    assert product.quantity == 10


def test_set_valid_price(capfd):
    product = Product("Продукт", "Описание", 1000.0, 2)
    product.price = 800
    assert product.price == 800


def test_set_negative_price(capfd):
    product = Product("Продукт", "Описание", 1000.0, 2)
    product.price = -500
    assert product.price == 1000.0


def test_set_zero_price(capfd):
    product = Product("Продукт", "Описание", 1000.0, 2)
    product.price = 0

    assert product.price == 1000.0


@pytest.fixture()
def smartphone_redmi():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


def test_init_smartphone(smartphone_redmi):
    assert smartphone_redmi.name == "Xiaomi Redmi Note 11"
    assert smartphone_redmi.description == "1024GB, Синий"
    assert smartphone_redmi.price == 31000.0
    assert smartphone_redmi.quantity == 14
    assert smartphone_redmi.efficiency == 90.3
    assert smartphone_redmi.model == "Note 11"
    assert smartphone_redmi.memory == 1024
    assert smartphone_redmi.color == "Синий"


@pytest.fixture()
def lawngrass_elit():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_init_lawngrass(lawngrass_elit):
    assert lawngrass_elit.name == "Газонная трава"
    assert lawngrass_elit.description == "Элитная трава для газона"
    assert lawngrass_elit.price == 500.0
    assert lawngrass_elit.quantity == 20
    assert lawngrass_elit.country == "Россия"
    assert lawngrass_elit.germination_period == "7 дней"
    assert lawngrass_elit.color == "Зеленый"
