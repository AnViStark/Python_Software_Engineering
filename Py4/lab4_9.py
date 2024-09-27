import datetime as dt

def date():
    value = int(input("Введите число: "))
    today = dt.date.today()
    future = today + dt.timedelta(days=value)
    print(f"День недели через {value} дней: {future.isoweekday()}")


if __name__ == '__main__':
    print(f"Сегодня: {dt.date.today()}. День недели - {dt.date.today().isoweekday()}")
    date()