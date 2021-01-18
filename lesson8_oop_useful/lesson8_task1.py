def should_be_true(func):
    def check_true(assertions):
        is_assertions_true = True
        for (key, check) in func(assertions).items():
            if not check:
                print(f"некорректно: {key}")
                is_assertions_true = False
            else:
                print(f"корректно: {key}")
        return is_assertions_true
    return check_true


def check_year_is_leap(year):
    if year % 400 == 0:
        return True
    else:
        if (year % 4 == 0) & (year % 100 != 0):
            return True
        else:
            return False


def check_year_is_correct(year):
    if (year > 0) & (year < 10000):
        return True
    return False


def check_month_is_correct(month):
    if (month >= 1) & (month <= 12):
        return True
    return False


def check_day_is_correct(day, month, year):
    if (day > 0) & (day <= 31):
        if month in [4, 6, 9, 11]:
            if day > 30:
                return False
        elif month == 2:
            if check_year_is_leap(year):
                if day > 29:
                    return False
            else:
                if day > 28:
                    print("Если год невисокосный, в феврале может быть максимум 28 дней")
                    return False
        return True
    return False


class Date:
    dates = []

    def __init__(self, date):
        self.date = date

    @classmethod
    def get_day_month_year(cls, date):
        cls.dates = [int(date_part) for date_part in date.split("-")]

    @staticmethod
    @should_be_true
    def check_array(dates: []):
        return {f"День {dates[0]}": check_day_is_correct(dates[0], dates[1], dates[2]),
                f"Месяц {dates[1]}": check_month_is_correct(dates[1]),
                f"Год {dates[2]}": check_year_is_correct(dates[2])}


for date in ["28-02-2021", "29-02-2021", "29-02-2020"]:
    x = Date(date)
    print(f"Проверить на корректность дату {x.date} :")
    x.get_day_month_year(date)
    print(f"Дата корректна? {x.check_array(Date.dates)} \n")
