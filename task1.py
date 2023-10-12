from datetime import datetime, timedelta, date


def get_congratulation_day(day_str: str):
    if day_str in ['Sunday', 'Saturday']:
        return 'Monday'

    return day_str


def get_birthdays_per_week(users):
    today_dt = datetime.today().date()

    days = {}
    for user in users:
        if ('birthday' not in user or
                not isinstance(user['birthday'], date) or
                'name' not in user or
                not isinstance(user['name'], str)):
            continue

        user_bd = user['birthday'].date()
        try:
            bday_this_year = user_bd.replace(year=today_dt.year)
        except ValueError:
            # user is born in a leap year, celebration is shifted to 28.02
            prev_day = user_bd.day - 1
            bday_this_year = user_bd.replace(year=today_dt.year, day=prev_day)

        delta_days = (bday_this_year - today_dt).days

        # > 0 to show only preceeding birthdays
        if delta_days < 7 and delta_days > 0:
            birthday_week_day = bday_this_year.strftime('%A')
            congratulation_day = get_congratulation_day(birthday_week_day)

            if congratulation_day not in days:
                days[congratulation_day] = []
            days[congratulation_day].append(user['name'])

    result = {}
    # to show days of week starting from today
    for i in range(0, 7):
        dt = (datetime.now() + timedelta(days=i)).date()
        day_in_week = dt.strftime('%A')

        if day_in_week in days:
            result[day_in_week] = days[day_in_week]

    return result


if __name__ == '__main__':
    users = [
        {"name": "Jhon", "birthday": datetime(1955, 10, 17)},
        {"name": "Jack", "birthday": datetime(1977, 10, 15)},
        {"name": "Odrey", "birthday": datetime(1985, 10, 18)},
        {"name": "Bill", "birthday": datetime(1993, 10, 12)},
        {"name": "Jaycob", "birthday": datetime(1966, 10, 10)},
        {"name": "Lindon", "birthday": datetime(2000, 10, 14)},
        {"name": "Tifany", "birthday": datetime(2005, 10, 19)},
        {"name": "David", "birthday": datetime(1965, 10, 21)},
        {"name": "Alex", "birthday": datetime(1953, 10, 22)}
    ]
    result = get_birthdays_per_week(users)
    for day in result.keys():
        print('{}: {}'.format(day, ', '.join(result[day])))
