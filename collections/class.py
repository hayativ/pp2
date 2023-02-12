class Person:
    def __init__(self, name: str, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

p = Person("Alikhan", 19)
print(p.name)
print(p.age)
print(p.getName())

# class Snake:
