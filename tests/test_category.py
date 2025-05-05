import pytest

from src.category import Category


@pytest.fixture
def reset_class_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_product(reset_class_counters):
    return Category('Продукты',
                    'Продукты для приготовления торта',
                    ["молоко", "сахар", "мука", "яйца", "шоколад"])


def test_init(category_product):
    assert category_product.name == 'Продукты'
    assert category_product.description == 'Продукты для приготовления торта'
    assert category_product.products == ["молоко", "сахар", "мука", "яйца", "шоколад"]


def test_class_attribute_counts_single(category_product):
    assert Category.category_count == 1
    assert Category.product_count == 5


def test_class_attribute_counts_multiple(reset_class_counters):
    cat1 = Category('Овощи', 'Свежие овощи', ["огурец", "помидор"])
    cat2 = Category('Фрукты', 'Свежие фрукты', ["яблоко", "груша", "банан"])

    assert cat1.description == 'Свежие овощи'
    assert cat2.products == ["яблоко", "груша", "банан"]
    assert Category.category_count == 2
    assert Category.product_count == 5
