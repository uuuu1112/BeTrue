import datetime

def beforeDays(days):
    today=datetime.date.today()
    beforeDays=datetime.timedelta(days=days)
    return today-beforeDays