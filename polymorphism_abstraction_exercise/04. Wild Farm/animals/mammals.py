from project1.animals.animal import Mammal
from project1.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Fruit, Vegetable]
        self.weight_per_food = 0.1

    def make_sound(self):
        return "Squeak"

    # def feed(self, food):
    #     if type(food) != Vegetable or type(food) != Fruit:
    #         return f"Mouse does not eat {type(food)}!"
    #     self.weight += (0.1 * food.quantity)


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.4

    def make_sound(self):
        return "Woof!"

    # def feed(self, food):
    #     if type(food) != Meat:
    #         return f"Dog does not eat {type(food)}!"
    #     self.weight += (0.4 * food.quantity)


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat, Vegetable]
        self.weight_per_food = 0.3

    def make_sound(self):
        return "Meow"

    # def feed(self, food):
    #     if type(food) != Meat or type(food) != Vegetable:
    #         return f"Cat does not eat {type(food)}!"
    #     self.weight += (0.3 * * food.quantity)


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"

    # def feed(self, food):
    #     if type(food) != Meat:
    #         return f"Tiger does not eat {type(food)}!"
    #     self.weight += food.quantity

