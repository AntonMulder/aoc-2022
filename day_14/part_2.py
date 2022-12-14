import re

from utils.io import readlines
from utils.point import Point

DOWN = Point(1, 0)
LEFT_DOWN = Point(1, -1)
RIGHT_DOWN = Point(1, 1)


def run(puzzle_input):
    rocks = set()

    for line in puzzle_input:
        previous_point = None
        for x, y in re.findall(r"(\d+),(\d+)", line):
            p = Point(int(y), int(x))

            if previous_point:
                if previous_point.x == p.x:
                    # Vertical line
                    for delta_y in range(min(previous_point.y, p.y), max(previous_point.y, p.y) + 1):
                        rocks.add(Point(delta_y, p.x))
                else:
                    # Horizontal line
                    for delta_x in range(min(previous_point.x, p.x), max(previous_point.x, p.x) + 1):
                        rocks.add(Point(p.y, delta_x))
            previous_point = p

    bottom = max(rock.y for rock in rocks) + 2
    for x in range(-1000, 1000):
        rocks.add(Point(bottom, x))

    grain = 0
    while True:
        sand = Point(0, 500)

        while True:
            if sand + DOWN not in rocks:
                sand += DOWN
            elif sand + LEFT_DOWN not in rocks:
                sand += LEFT_DOWN
            elif sand + RIGHT_DOWN not in rocks:
                sand += RIGHT_DOWN
            else:
                if sand == Point(0, 500):
                    return grain + 1
                break

        rocks.add(sand)
        grain += 1


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
