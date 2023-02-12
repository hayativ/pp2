d = {}

d['Alikhan'] = 19
d['Anita'] = ['Statistics', 'Physics']

print(d.get('Anita'))

arr = d.items()
# print(arr)

print(d)
d.pop('Anita')
print(d)

d['test'] = { "id" : 2, "name" : "Alikhan" } 