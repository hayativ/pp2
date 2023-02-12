from datetime import datetime

d1 = datetime.now()
d2 = datetime(2003, 3, 7)

d = d1 - d2
print(d.days)