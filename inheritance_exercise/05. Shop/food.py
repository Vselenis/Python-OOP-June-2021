from project1.product import Product

QUANTITY_FOOD = 15
class Food(Product):
    def __init__(self, name):
        super().__init__(name, QUANTITY_FOOD)

