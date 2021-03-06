from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.rooms.room import Room
from project.appliances.tv import TV


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2
        self.calculate_expenses(self.appliances)