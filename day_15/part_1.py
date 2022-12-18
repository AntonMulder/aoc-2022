import re

from utils.io import readlines
from utils.point import Point

SENSOR_RE = re.compile(r"Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)")


def run(puzzle_input, y=2000000):
    cannot_contain = set()
    for sensor_line in puzzle_input:
        sensor_x, sensor_y, beacon_x, beacon_y = SENSOR_RE.match(sensor_line).groups()
        sensor = Point(int(sensor_y), int(sensor_x))
        beacon = Point(int(beacon_y), int(beacon_x))

        distance = sensor.distance(beacon)

        for x in range(sensor.x - distance, sensor.x + distance):
            p = Point(y, x)

            if sensor.distance(p) <= distance and p != beacon:
                cannot_contain.add(p)

    return len(cannot_contain)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
