import datetime


def date_format(date: datetime, format: str = "%Y-%m-%d"):
    return date.strftime(format)
