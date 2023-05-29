"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import *

def print_days():
    dt_now = datetime.now()
    delta_1 = timedelta(days=1)
    delta_30 = timedelta(days=30)
    yesterday = dt_now - delta_1
    month_ago = dt_now - delta_30
    print(yesterday, dt_now, month_ago, sep='\n')


def str_2_datetime(date_string):
    str_dt = datetime.strptime(date_string + '', "%d/%m/%y %H:%M:%S.%f")
    return(str_dt)
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
