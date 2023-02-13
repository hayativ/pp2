# b. Write a program to create an iterator that yields the first n elements of a list.
class FirstNElements:
    def __inint__(self, lst, n):
        self.lst = lst
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self) :
        if self.current >= self.n:
            raise StopIteration
        value = self.lst[self.current]
        self.current += 1
        return value
first_n_elements = FirstNElements ([1, 2, 3, 4, 5], 3)
for number in first_n_elements:
    print(number)
