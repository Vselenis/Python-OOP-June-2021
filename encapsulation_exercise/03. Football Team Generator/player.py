class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value


    def __str__(self):
        return f"Player: {self.name}\nSprint: {self.sprint}\nDribble: {self.dribble}\nPassing: {self.passing}\nShooting: {self.shooting}"

