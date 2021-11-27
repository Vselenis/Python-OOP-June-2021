class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.result = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.result < self.number:
            idx = self.result
            self.result += 1
            return self.sequence[idx % len(self.sequence)]

        else:
            raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
