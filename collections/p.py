arr = list(map(int, input().split()))

min_element, max_element = 1e9, -1e9
min_element_i, max_element_i = 1e9, -1e9

for i in range(0, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
        min_element_i = i

for i in range(0, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
        max_element_i = i

arr[min_element_i], arr[max_element_i] = arr[max_element_i], arr[min_element_i]
for i in arr:
    print(i, end=" ")