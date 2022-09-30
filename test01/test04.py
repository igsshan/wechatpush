from datetime import date, datetime, timedelta

# today = datetime.now()

# print(datetime.datetime.now() + datetime.timedelta(days=1)).strftime()

dayTime = datetime.strftime(datetime.now() + timedelta(days=1), "%Y-%m-%d %H:%M:%S")
# print(dayTime)

before = datetime.now() + timedelta(days=1)
# print(before)

today = datetime.now() + timedelta(days=1)
print(today)
