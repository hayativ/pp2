# c. Write a program to create an iterator that yields the squares of the numbers in a list.
class SquaredElements:
    def __inint__(self, lst, n):
        self.lst = lst
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self) :
        if self.current >= len(self.lst):
            raise StopIteration
        value = self.lst[self.current] ** 2
        self.current += 1
        return value
squared_elements = SquaredElements([1, 2, 3, 4, 5])
for number in squared_elements:
    print(number)
