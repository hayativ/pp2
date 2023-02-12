# && = and
# || = or

arr = list(map(int, input().split()))

for i in range(0, len(arr) - 1):
    if arr[i] * arr[i + 1] > 0:
        print(arr[i], arr[i + 1]) 
        exit()