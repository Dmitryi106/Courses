class Product():
    name: str
    description: str
    price: float
    quantily: int

    def __init__(self, name, description, price, quantily):
        self.name = name
        self.description = description
        self.price = price
        self.quantily = quantily
