import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def reset_class_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_product(reset_class_counters):
    p1 = Product("Молоко", "Для теста", 80.0, 1)
    p2 = Product("Сахар", "Сладкий", 50.0, 2)
    p3 = Product("Мука", "Пшеничная", 40.0, 3)
    p4 = Product("Яйца", "Куриные", 70.0, 4)
    p5 = Product("Шоколад", "Черный", 100.0, 5)

    return Category("Продукты", "Продукты для приготовления торта", [p1, p2, p3, p4, p5])


def test_type_error_in_add_product():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1]
    )
    with pytest.raises(TypeError):
        product1 + category1


def test_type_error_in_add():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_str_category(category_product):
    assert str(category_product) == "Продукты, количество продуктов: 15 шт."


def test_init(category_product):
    assert category_product.name == "Продукты"
    assert category_product.description == "Продукты для приготовления торта"
    # Проверим строку
    expected = (
        "Молоко, 80.0 руб. Остаток: 1 шт.\n"
        "Сахар, 50.0 руб. Остаток: 2 шт.\n"
        "Мука, 40.0 руб. Остаток: 3 шт.\n"
        "Яйца, 70.0 руб. Остаток: 4 шт.\n"
        "Шоколад, 100.0 руб. Остаток: 5 шт."
    )
    assert category_product.products == expected


def test_class_attribute_counts_single(category_product):
    assert Category.category_count == 1
    assert Category.product_count == 5


def test_class_attribute_counts_multiple(reset_class_counters):
    p1 = Product("Огурец", "Свежий", 30.0, 5)
    p2 = Product("Помидор", "Красный", 35.0, 6)
    p3 = Product("Яблоко", "Зелёное", 25.0, 7)
    p4 = Product("Груша", "Спелая", 28.0, 8)
    p5 = Product("Банан", "Жёлтый", 22.0, 9)

    cat1 = Category("Овощи", "Свежие овощи", [p1, p2])
    cat2 = Category("Фрукты", "Свежие фрукты", [p3, p4, p5])

    assert cat1.description == "Свежие овощи"
    assert "Груша" in cat2.products
    assert Category.category_count == 2
    assert Category.product_count == 5


def test_add_product(reset_class_counters):
    # Создаем начальный продукт и категорию
    p1 = Product("Мука", "Пшеничная", 50.0, 10)
    category = Category("Ингредиенты", "Для выпечки", [p1])

    # Проверим, что один продукт в начале
    assert Category.product_count == 1

    # Добавим новый продукт
    p2 = Product("Сахар", "Белый", 60.0, 5)
    category.add_product(p2)

    # Проверим, что продукт добавлен
    assert "Сахар" in category.products

    # Проверим, что общий счетчик увеличился
    assert Category.product_count == 2


@pytest.fixture
def category():
    return Category("Электроника", "Гаджеты", [])


def test_add_invalid_product(category):
    with pytest.raises(TypeError):
        category.add_product("не продукт")
