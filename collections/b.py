arr = list(map(int, input().split()))

# for i in range(0, len(arr)):
#     if arr[i] % 2 == 0:
#         print(arr[i], end=" ")

for el in arr:
    if el % 2 == 0:
        print(el, end=" ")