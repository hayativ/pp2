from datetime import datetime

d1 = datetime.now()
d2 = datetime(2005, 3, 30)

d = d1 - d2
print(d.days // 30.5 / 12)