import re

from utils.io import readlines
from utils.point import Point

SENSOR_RE = re.compile(r"Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)")


def run(puzzle_input):
    sensors = set()
    beacons = set()
    for sensor_line in puzzle_input:
        sensor_x, sensor_y, beacon_x, beacon_y = SENSOR_RE.match(sensor_line).groups()

        beacon = Point(int(beacon_y), int(beacon_x))
        beacons.add(beacon)

        sensor = Point(int(sensor_y), int(sensor_x))
        distance = sensor.distance(beacon)
        sensors.add((sensor, distance))

    def _is_distress_beacon(p):
        for sensor, distance in sensors:
            if sensor.distance(p) <= distance and p not in beacons:
                return False
        return True

    for sensor, distance in sensors:
        for delta_x in range(distance + 2):
            delta_y = (distance + 1) - delta_x
            for neighbor in [Point(-1, 1), Point(1, -1), Point(-1, -1), Point(1, 1)]:
                p = sensor + Point(delta_y * neighbor.y, delta_x * neighbor.x)
                if not (0 <= p.x <= 4000000 and 0 <= p.y <= 4000000):
                    continue
                if _is_distress_beacon(p):
                    return p.x * 4_000_000 + p.y


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
