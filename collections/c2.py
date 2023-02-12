arr = list(map(int, input().split()))

arr = [i for i in arr if i > 0]
print(len(arr))