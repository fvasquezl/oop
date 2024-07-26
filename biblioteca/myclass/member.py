from dataclasses import dataclass, field
from typing import List

from .book import Book


@dataclass
class Member:
    name: str = field(default="")
    address: str = field(default="")
    borrowed_books: List[Book] = field(default_factory=list)

    def __repr__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Address:{self.address}\n"
            f"Books:{self.borrowed_books}\n"
        )
