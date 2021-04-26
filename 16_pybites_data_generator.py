from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)
TODAY = datetime.today()


def gen_special_pybites_dates():
    current_datetime = PYBITES_BORN
    one_hundred_days = timedelta(days=100)
    while current_datetime < TODAY:
        yield current_datetime + one_hundred_days
        current_datetime += one_hundred_days

