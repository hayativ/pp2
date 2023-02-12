from math import sqrt

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
        self.x = int(input("Enter new coordinates for X: "))
        self.y = int(input("Enter new coordinates for Y: "))

    def dist(self, x1, y1):
        return sqrt((self.x - x1)**2 + (self.y - y1)**2)

p = Point(0, 0)
p.move()
print(p.dist(2, 2))
print(p.dist(int(input()), int(input())))