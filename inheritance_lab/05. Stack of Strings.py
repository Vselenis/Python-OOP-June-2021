class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def top(self):
        return self.data[-1]

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'

