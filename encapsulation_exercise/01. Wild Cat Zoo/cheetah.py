from project1.animal import Animal

class Cheetah(Animal):
    GET_NEEDS = 60
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Cheetah.GET_NEEDS)
