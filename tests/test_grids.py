from pathlib import Path
from typing import Iterable

import pytest

from days360 import days360_EU, days360_US, days360_US_NASD

from .conftest import ExpectedResult, cases_from_csv_grid

DATA = Path("tests") / "data"


@pytest.mark.parametrize(
    "func,cases",
    (
        (days360_EU, cases_from_csv_grid(DATA / "calc_DAYS360_EU.csv")),
        (days360_US, cases_from_csv_grid(DATA / "calc_DAYS360_US.csv")),
        (days360_EU, cases_from_csv_grid(DATA / "excel_DAYS360_EU.csv")),
        (days360_US, cases_from_csv_grid(DATA / "excel_DAYS360_US.csv")),
        (days360_US_NASD, cases_from_csv_grid(DATA / "NASD_reference_DAYS360_US.csv")),
    ),
)
def test_grids(func, cases: Iterable[ExpectedResult]):
    for case in cases:
        assert func(case.start, case.end) == case.days
