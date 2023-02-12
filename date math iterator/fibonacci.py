class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            self.n -= 1
            self.current, self.next = self.next, self.current + self.next
            return self.current
        else:
            raise StopIteration

fib = Fibonacci(10)
for i in fib:
    print(i, end=" ")
print()