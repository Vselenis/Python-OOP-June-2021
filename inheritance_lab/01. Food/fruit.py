from project1.food import Food

class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

f = Fruit("banana", "2030")
print(f.expiration_date)
