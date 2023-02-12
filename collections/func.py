def sayHello():
    print("hello")

sayHello()

def sayHello() -> int:
    print("hello")

print(sayHello())

def twoSum(a: int, b: int) -> int:
    return a + b

print(twoSum(5, 7))