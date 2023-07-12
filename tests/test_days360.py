from datetime import date

from days360 import days360_EU, days360_US
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

    # from https://www.mathworks.com/help/finance/days360e.html
    assert days360_EU(date(2022, 1, 1), date(2022, 2, 1)) == 30


def test_day360_US():
    assert days360_US(date(2012, 1, 23), date(2012, 12, 31)) == 338
    assert days360_US(date(2012, 3, 19), date(2012, 12, 31)) == 282
    assert days360_US(date(2012, 1, 1), date(2012, 12, 31)) == 360
    
    # from https://www.mathworks.com/help/finance/days360.html
#     NumDays = days360(datetime(2000,1,15) , datetime(2000,3,15))
# NumDays = 60
# Determine the NumDays using a datetime array for EndDate.

# MoreDays = [datetime(2000,3,15) ; datetime(2000,4,15) ; datetime(2000,6,15)];
# NumDays = days360(datetime(2000,1,15), MoreDays)
# NumDays = 3×1

#     60
#     90
#    150


# https://www.mathworks.com/help/finance/days360psa.html
# StartDate = '1-Jan-2002';
# EndDate = '1-Feb-2002';
# NumDays = days360psa(StartDate, EndDate)
# NumDays = 30
# Determine the NumDays in the month of January using datetimes for StartDate and EndDate.

# NumDays = days360psa(datetime(2002,1,1) , datetime(2002,2,1))
# NumDays = 30
# Determine the NumDays using a datetime array for EndDate.

# MoreDays = [datetime(2000,3,15) ; datetime(2000,4,15) ; datetime(2000,6,15)];
# NumDays = days360psa(datetime(2000,1,15), MoreDays)
# NumDays = 3×1

#     60
#     90
#    150


# https://www.mathworks.com/help/finance/days360isda.html
# StartDate = '1-Jan-2002';
# EndDate = '1-Feb-2002';
# NumDays = days360isda(StartDate, EndDate)
# NumDays = 30
# Determine the NumDays in the month of January using datetimes for StartDate and EndDate.

# NumDays = days360isda(datetime(2002,1,1), datetime(2002,2,1))
# NumDays = 30
# Determine the NumDays using a datatime array for EndDate.

# MoreDays = [datetime(2000,3,15) ; datetime(2000,4,15) ; datetime(2000,6,15)];
# NumDays = days360isda(datetime(2000,1,15), MoreDays)
# NumDays = 3×1

#     60
#     90
#    150
