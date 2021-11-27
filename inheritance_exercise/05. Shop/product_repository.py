from project1.drink import Drink
from project1.food import Food
from project1.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []


    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for p in self.products:
            if p.name == product_name:
                return p


    def remove(self, product_name):
        p = self.find(product_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        result = [f"{x.name}: {x.quantity}" for x in self.products]
        return "\n".join(result)
