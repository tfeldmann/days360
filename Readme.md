# days360

[![Tests](https://github.com/tfeldmann/days360/actions/workflows/tests.yml/badge.svg)](https://github.com/tfeldmann/days360/actions/workflows/tests.yml)
<a href="https://pypi.org/project/days360/">
  <img src="https://img.shields.io/pypi/v/days360" title="PyPI Version">
</a>

Calculates the days between two dates based on the 360-day year.

- Implementation of Excel's (or Number's) `DAYS360` / `TAGE360` formula in python.
- Both EU and US methods of calculation are supported, with optional Excel bug compatibility.

## Installation

```
pip install days360
```

## Usage

```python
from datetime import date
from days360 import days360

date_a = date(2022, 10, 2)
date_b = date(2023, 11, 30)

# supported methods: "US" (default), "US_NASD", "EU"
days = days360(date_a, date_b, method="US")
print(days)  # prints 418
```

## Planned

- ISDA and PSA methods.

## Notes and credits

- Implementations are based on https://en.wikipedia.org/wiki/360-day_calendar.
- This library started as a port of this ruby gem: https://github.com/tamaloa/days360/tree/master
