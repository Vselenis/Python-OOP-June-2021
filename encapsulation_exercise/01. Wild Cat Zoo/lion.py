from project1.animal import Animal

class Lion(Animal):
    GET_NEEDS = 50
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.GET_NEEDS)
