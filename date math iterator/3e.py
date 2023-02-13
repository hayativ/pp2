# e. Write a program to create an iterator that yields the elements of a list in reverse order.
class ReverseElements:
    def __inint__(self, lst, n):
        self.lst = lst
        self.current = len(self.lst) - 1
    def __iter__(self):
        return self
    def __next__(self) :
        if self.current < 0:
            raise StopIteration
        value = self.lst[self.current]
        self.current -= 1
        return value
reverse_elements = ReverseElements ([1, 2, 3, 4, 5])
for number in reverse_elements:
    print(number, end= " ")
