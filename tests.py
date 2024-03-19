import pytest

from main import Category
from main import Product


@pytest.fixture()
def category_test():
    return Category("Личная гигиена", "Предметы для личной гигены", "Мыло")


def test_init(category_test):
    assert category_test.name == 'Личная гигиена'
    assert category_test.description == 'Предметы для личной гигены'
    assert category_test.prod == 'Мыло'
    assert category_test.num_ctg == 1
    assert category_test.uniq_prod == 4


@pytest.fixture()
def product_test():
    return Product("Мыло", "Мыло - это мыло!", 10.4, 4)


def prdct_init_2(product_test):
    assert product_test.name == 'Мыло'
    assert product_test.descritpion == 'Мыло - это мыло!'
    assert product_test.price == 11.4
    assert product_test.amount == 4
