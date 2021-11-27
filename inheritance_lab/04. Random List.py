import random


class RandomList(list):
    def get_random_element(self):
        remove_value = random.choice(self)
        self.remove(remove_value)
        return remove_value


random_list = RandomList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(random_list)
print(random_list.get_random_element())
print(random_list)
