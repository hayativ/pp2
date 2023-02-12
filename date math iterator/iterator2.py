class Iterator:
    def __init__(self):
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

nums = Iterator()

print(next(nums.__iter__()))