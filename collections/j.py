arr = list(map(int, input().split()))
x = int(input())

arr.append(x)
arr.sort(reverse=True)

for i in range(0, len(arr) - 1):
    if arr[i] == x and arr[i] > arr[i + 1]:
        print(i + 1)
        exit()

if arr[len(arr) - 1] == x:
    print(len(arr))