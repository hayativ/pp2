class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f"{self.name}: Hello!")

class Student(Person):
    def __init__(self, name: str, age: int, id: str):
        super().__init__(name, age)
        self.id = id

s = Student("Alikhan", 19, "21B0")
print(s.sayHello())