from datetime import date

import pytest

from days360 import days360_EU, days360_US, days360_US_NASD
from days360.days360 import is_last_day_of_february


def test_last_day_of_february():
    assert not is_last_day_of_february(date(2012, 1, 1))
    assert not is_last_day_of_february(date(2012, 2, 10))
    assert not is_last_day_of_february(date(2012, 2, 28))
    assert is_last_day_of_february(date(2012, 2, 29))
    assert is_last_day_of_february(date(2007, 2, 28))
    assert not is_last_day_of_february(date(2012, 1, 31))


def test_days360_EU():
    # From http://zinsmethoden.de/#
    date_a = date(2003, 11, 18)
    date_b = date(2004, 3, 18)
    assert days360_EU(date_a, date_b) == 120


def test_day360_US():
    assert days360_US(date(2012, 1, 23), date(2012, 12, 31)) == 338
    assert days360_US(date(2012, 3, 19), date(2012, 12, 31)) == 282
    assert days360_US(date(2012, 1, 1), date(2012, 12, 31)) == 360


def test_apple_numbers_examples():
    # =TAGE360("20.12.2008";"31.03.2009") liefert den Ergebniswert 101T.
    assert days360_US(date(2008, 12, 20), date(2009, 3, 31)) == 101
    # =TAGE360("27.2.2008";"31.3.2009";0) liefert den Ergebniswert 394T.
    assert days360_US(date(2008, 2, 27), date(2009, 3, 31)) == 394
    # =TAGE360("27.2.2008";"31.03.2009";1) liefert den Ergebniswert 393T, da die
    # europäische Berechnungsmethode verwendet wird.
    assert days360_EU(date(2008, 2, 27), date(2009, 3, 31)) == 393


@pytest.mark.parametrize("func", (days360_US, days360_EU, days360_US_NASD))
def test_mathworks_examples(func):
    # from https://www.mathworks.com/help/finance/days360.html
    assert func(date(2022, 1, 1), date(2022, 2, 1)) == 30
    assert func(date(2000, 1, 15), date(2000, 3, 15)) == 60
    assert func(date(2000, 1, 15), date(2000, 3, 15)) == 60
    assert func(date(2000, 1, 15), date(2000, 4, 15)) == 90
    assert func(date(2000, 1, 15), date(2000, 6, 15)) == 150
    # from https://www.mathworks.com/help/finance/days360e.html
    # https://www.mathworks.com/help/finance/days360psa.html
    # https://www.mathworks.com/help/finance/days360isda.html
