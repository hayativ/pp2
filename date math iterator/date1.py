from datetime import datetime

print(datetime.now())

d = datetime.now()
print(d.day)
print(d.month)
print(d.year)

d2 = datetime(2003, 3, 7)

# y Y - short and long version of year
dateFormat = "%d:%m:%y"
print(d2.strftime(dateFormat))

dateFormat2 = "%A"
print(d2.strftime(dateFormat2))

dateFormat3 = "%a"
print(d2.strftime(dateFormat3))