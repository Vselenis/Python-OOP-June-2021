from project1.product import Product

QUANTITY_DRINK = 10
class Drink(Product):
    def __init__(self, name):
        super().__init__(name, QUANTITY_DRINK)
