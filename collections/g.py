# arr = list(map(int, input().split()))

# max_element = -1e9
# max_index = -1
# # range [)
# for i in range(0, len(arr)):
#     if arr[i] > max_element:
#         max_element = arr[i]
#         max_index = i

# print(max_element, max_index)

a = list(map(int, input().split()))

max = a[0]
index = 0
for i, element in enumerate(a):
    if max < element:
        max = element
        index = i
print(max, index)