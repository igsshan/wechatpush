from datetime import date, datetime

today = datetime.now()
chunjie = "01-22"
yuandan = "01-01"


def get_yuandan():
    next = datetime.strptime(str(datetime.today().strftime("%Y")) + "-" + yuandan, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


print(get_yuandan())


def get_chunjie():
    next = datetime.strptime(str(datetime.today().strftime("%Y")) + "-" + chunjie, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


print(get_chunjie())
