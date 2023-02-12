# Task for Classes / Inheritance
# Make 2 classes: User, Student
# Do not forget about inheritance
# Note:
# User: id (string), name (string), login(method)
# Student: id (string), name(string), login(method), 
# participate lesson(method)

class User:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name

    def login(self) -> None:
        print(f'{self.name} login')

class Student(User):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)

    def participate(self) -> None:
        print(f"{self.name} participate")

u = User("21BD", "Alikhan")
s1 = Student("22BD1", "Anita")
s2 = Student("22BD2", "Zhaniya")

u.login()
s1.login()
s2.login()

arr = [s1, s2]