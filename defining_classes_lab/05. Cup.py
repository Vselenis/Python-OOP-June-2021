class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def get_free_size(self):
        return self.size - self.quantity

    def fill(self, mililiters):
        if self.get_free_size() < mililiters:
            return

        self.quantity += mililiters

    def status(self):
        return self.get_free_size()
