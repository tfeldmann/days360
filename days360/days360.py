"""
Implementation as given by https://en.wikipedia.org/wiki/360-day_calendar
"""
from datetime import date as Date
from datetime import timedelta
from typing import Literal

Method = Literal["US", "US_NASD", "EU"]


def is_last_day_of_february(date: Date) -> bool:
    last_february_day_in_given_year = Date(date.year, 3, 1) + timedelta(days=-1)
    return date == last_february_day_in_given_year


def days360_US(
    date_a: Date, date_b: Date, preserve_excel_compatibility: bool = True
) -> int:
    """
    This method uses the the US/NASD Method (30US/360) to calculate the days between two
    dates.

    NOTE: to use the reference calculation method 'preserve_excel_compatibility' must be
    set to false.
    The default is to preserve compatibility. This means results are comparable to those
    obtained with Excel or Calc.
    This is a bug in Microsoft Office which is preserved for reasons of backward
    compatibility. Open Office Calc also choose to "implement" this bug to be MS-Excel
    compatible [1].

    [1] http://wiki.openoffice.org/wiki/Documentation/How_Tos/Calc:_Date_%26_Time_functions#Financial_date_systems
    """
    day_a = date_a.day
    day_b = date_b.day

    # Step 1 must be skipped to preserve Excel compatibility
    # (1) If both date A and B fall on the last day of February, then date B will be
    # changed to the 30th.
    if (
        not preserve_excel_compatibility
        and is_last_day_of_february(date_a)
        and is_last_day_of_february(date_b)
    ):
        day_b = 30

    # (2) If date A falls on the 31st of a month or last day of February, then date A
    # will be changed to the 30th.
    if day_a == 31 or is_last_day_of_february(date_a):
        day_a = 30

    # (3) If date A falls on the 30th of a month after applying (2) above and date B
    # falls on the 31st of a month, then date B will be changed to the 30th.
    if day_a == (30) and day_b == (31):
        day_b = 30

    days = (
        (date_b.year - date_a.year) * 360
        + (date_b.month - date_a.month) * 30
        + (day_b - day_a)
    )
    return days


def days360_US_NASD(date_a: Date, date_b: Date) -> int:
    return days360_US(date_a, date_b, preserve_excel_compatibility=False)


def days360_EU(date_a: Date, date_b: Date) -> int:
    """
    This method uses the the European method (30E/360) to calculate the days between two
    dates
    """
    day_a = date_a.day
    day_b = date_b.day

    # If either date A or B falls on the 31st of the month, that date will be changed to
    # the 30th
    if day_a == 31:
        day_a = 30
    if day_b == 31:
        day_b = 30

    # Where date B falls on the last day of February, the actual date B will be used.
    # This rule is actually only a note and does not change the calculation.

    days = (
        (date_b.year - date_a.year) * 360
        + (date_b.month - date_a.month) * 30
        + (day_b - day_a)
    )
    return days


def days360(date_a: Date, date_b: Date, method: Method = "US") -> int:
    if method == "US":
        return days360_US(date_a, date_b)
    elif method == "US_NASD":
        return days360_US_NASD(date_a, date_b)
    elif method == "EU":
        return days360_EU(date_a, date_b)
    raise ValueError(f"Unknown method: {method}")
