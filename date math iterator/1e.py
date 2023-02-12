from datetime import datetime

d = datetime.now()
dateFormat = "%d-%m-%Y"

print(d.strftime(dateFormat))