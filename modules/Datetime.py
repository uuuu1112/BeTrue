import datetime

def beforeDays(days):
    today=datetime.date.today()
    beforeDays=datetime.timedelta(days=days)
    return today-beforeDays

def beforeMonthss(months):
    today=datetime.date.today()
    beforeMonths=datetime.timedelta(monthss=months)
    return today-beforeMonths

def test():
    return "test"