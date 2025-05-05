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
