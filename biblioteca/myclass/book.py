from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Book:
    title: str = field(default="")
    author: str = field(default="")
    _year: int = field(repr=False, default=0, init=False)
    _qty: int = field(repr=False, default=0, init=False)

    def __repr__(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Author:{self.author}\n"
            f"year: {self.year}\n"
            f"qty: {self.qty}"
        )

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        current_year = datetime.now().year
        if isinstance(value, int) and 1450 <= value <= current_year:
            self._year = value
        else:
            raise ValueError(f"Year must be an integer between 1450 and {current_year}")

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, value):
        if isinstance(value, int):
            self._qty = value
        else:
            raise ValueError("Quantity must be an integer")
