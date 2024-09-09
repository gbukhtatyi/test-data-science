from datetime import datetime


def diff_in_days(dt1, dt2):
    days_1 = datetime.strptime(dt1, '%Y-%m-%d').toordinal()
    days_2 = datetime.strptime(dt2, '%Y-%m-%d').toordinal()

    return abs(days_1 - days_2)


date_1 = "2023-08-01"
date_2 = "2024-09-09"

print('Результат:', diff_in_days(date_1, date_2))
