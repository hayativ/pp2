# 1)
with open("./text.txt", 'r') as file:
    f = file.read()
    # print(f)


# 2)
f = open("./text.txt", 'r')
print(f.read())