from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, b: int):
        return Point(self.x + b.x, self.y + b.y)

    def __sub__(self, b: int):
        return Point(self.x - b.x, self.y - b.y)
