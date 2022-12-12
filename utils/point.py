from typing import NamedTuple


class Point(NamedTuple):
    y: int
    x: int

    def __add__(self, b: int):
        return Point(self.y + b.y, self.x + b.x)

    def __sub__(self, b: int):
        return Point(self.y - b.y, self.x - b.x)


UP = Point(1, 0)
RIGHT = Point(0, 1)
DOWN = Point(-1, 0)
LEFT = Point(0, -1)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
