import pytest

from src.product import Product


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
    assert (product1 + product2) == 2580000


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
