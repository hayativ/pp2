# d. Write a program to create an iterator that yields the unique elements of a list.
class UniqueElements:
    def __inint__(self, lst, n):
        self.lst = lst
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self) :
        if self.current >= len(self.lst):
            raise StopIteration
        value = self.lst[self.current]
        self.current += 1
        return value
unique_elements = UniqueElements([1, 2, 3, 4, 5, 5, 6, 6])
for number in unique_elements:
    print(number)
