import datetime as dt

now = dt.datetime.now()

tomorrow = now + dt.timedelta(days = 1)
six_months = now + dt.timedelta(days = 6*30)

print(tomorrow.strftime("%d/%m/%Y"))
print(six_months.strftime("%d/%m/%Y"))