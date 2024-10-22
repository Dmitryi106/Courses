class Category():
    name: str
    description: str
    products: list

    total_category = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_category =+ 1
        Category.total_products =+ len(products)
