class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self) -> None:
        self.length = int(input("Enter square's length: "))

    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self) -> None:
        self.length = int(input("Enter rectangle's length: "))
        self.width = int(input("Enter rectangle's width: "))

    def area(self):
        return self.length * self.width


s = Square()
print(s.area())

r = Rectangle()
print(r.area())