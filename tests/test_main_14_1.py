from src.category import Category
from src.product import Product


def test_product_initialization():
    product = Product("Test Product", "Test Description", 999.99, 10)

    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 999.99
    assert product.quantity == 10


def test_category_initialization():
    product1 = Product("Prod 1", "Desc 1", 1000, 2)
    product2 = Product("Prod 2", "Desc 2", 2000, 5)

    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    category = Category("Test Category", "Category description", [product1, product2])

    assert category.name == "Test Category"
    assert category.description == "Category description"
    assert len(category.products) == 2
    assert product1 in category.products
    assert product2 in category.products

    assert Category.category_count == initial_category_count + 1
    assert Category.product_count >= initial_product_count + 2


def test_category_class_attributes():
    # Очистим атрибуты для чистого теста
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("P1", "D1", 100, 1)
