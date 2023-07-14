from csv import DictReader
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ExpectedResult:
    start: date
    end: date
    days: int


def cases_from_csv_grid(path: Path) -> Iterable[ExpectedResult]:
    with path.open("r") as f:
        for row in DictReader(f):
            start = date.fromisoformat(row.pop(""))
            for key, val in row.items():
                yield ExpectedResult(
                    start=start,
                    end=date.fromisoformat(key),
                    days=int(val) if val else 0,
                )
