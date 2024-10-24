import json

from src.Category import Category
from src.Product import Product


def load_data_from_json(Product):
    categories = []
    with open("Product.json",'r', encoding='UTF-8') as file:
        data = json.load(file)
        for category_data in data:
            products = []
            for product_data in category_data['products']:
                product = Product(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])
                products.append(product)
            category = Category(category_data['name'], category_data['description'], category_data['products'])
            categories.append(category)
        return categories
loaded = load_data_from_json(Product)
print(loaded[1].products[0]['name'])