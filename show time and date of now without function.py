from datetime import datetime
now = datetime.now()
FORMAT_DATE = "{:%Y-%m-%d, %H:%M:%S}".format(now)
print(FORMAT_DATE)
