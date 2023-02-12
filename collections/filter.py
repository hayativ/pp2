def isPrime(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter(arr: list) -> list:
    new_arr = []
    for i in arr:
        if isPrime(i):
            new_arr.append(i)
    return new_arr

arr = [1, 2, 3, 4, 5]
arr = filter(arr)
print(arr)