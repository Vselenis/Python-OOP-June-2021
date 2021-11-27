from project1.animals.animal import Bird
from project1.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if type(food) != Meat:
    #         return f"Owl does not eat {type(food)}!"
    #     self.weight += (0.25 * food.quantity)


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat, Vegetable, Fruit, Seed]
        self.weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"

    # def feed(self, food):
    #     self.weight += (0.35 * food.quantity)
