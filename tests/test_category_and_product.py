from src.category_and_priduct import Category


def test_product_init(some_product):
    assert some_product.name == 'Ноутбук'
    assert some_product.description == 'Игровой'
    assert some_product.price == 50000.0
    assert some_product.quantity == 10


def test_category_init(some_product, some_category):
    assert some_category.name == "Электроника"
    assert some_category.description == "Техника"
    assert len(some_category.products) == 1
    assert some_category.products[0] == some_product


def test_category_counter(some_category):
    assert Category.total_categories == 1


def test_total_products(some_category):
    assert Category.total_products == 1