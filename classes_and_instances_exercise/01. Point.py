import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x
        return self.x

    def set_y(self, new_y):
        self.y = new_y
        return self.y

    def distance(self, sec_x, sec_y):
        my_x = self.x - sec_x
        my_y = self.y - sec_y
        d = my_x ** 2 + my_y ** 2
        return math.sqrt(d)

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
