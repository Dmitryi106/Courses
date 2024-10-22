import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture()

def Category_test():
    return Category('Смартфоны', "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [["Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5],["Iphone 15", "512GB, Gray space", 210000.0, 8],["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14]])

def test_init_category(Category_test):
    assert Category_test.name == 'Смартфоны'
    assert Category_test.description =='Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert Category_test.products == [["Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5],["Iphone 15", "512GB, Gray space", 210000.0, 8],["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14]]
    assert Category_test.total_products == 3
    assert Category_test.total_category == 1

@pytest.fixture()

def Product_test():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init_product(Product_test):
    assert Product_test.name == "Samsung Galaxy C23 Ultra"
    assert Product_test.quantily == 5
    assert Product_test.price == 180000.0
    assert Product_test.description == "256GB, Серый цвет, 200MP камера"