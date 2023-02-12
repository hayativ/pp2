arr = list(map(int, input().split()))

for i in range(0, len(arr) - 1):
    if arr[i + 1] > arr[i]:
        print(arr[i + 1], end=" ")