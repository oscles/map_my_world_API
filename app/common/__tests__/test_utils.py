import datetime

from ..utils import date_format


def test_should_transform_date_to_default_format():
    date = datetime.datetime(2025, 1, 9)
    assert date_format(date) == "2025-01-09"


def test_should_transform_date_with_custom_format():
    date = datetime.datetime(2025, 1, 9)
    assert date_format(date, format="%d/%m/%Y") == "09/01/2025"
