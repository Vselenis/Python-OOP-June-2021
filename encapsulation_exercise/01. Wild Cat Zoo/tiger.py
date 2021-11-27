from project1.animal import Animal

class Tiger(Animal):
    GET_NEEDS = 45
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.GET_NEEDS)


