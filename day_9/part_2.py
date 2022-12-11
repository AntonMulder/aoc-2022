from utils.io import readlines
from utils.point import Point


def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0


def run(puzzle_input):
    directions = {"R": Point(0, 1), "L": Point(0, -1), "U": Point(1, 0), "D": Point(-1, 0)}
    rope = [Point(0, 0)] * 10
    visited = set(rope)

    for command in puzzle_input:
        direction, steps = command.split(" ")

        for step in range(int(steps)):
            rope[0] += directions[direction]

            for i in range(1, 10):
                delta = rope[i - 1] - rope[i]
                if abs(delta.x) > 1 or abs(delta.y) > 1:
                    rope[i] += Point(sign(delta.x), sign(delta.y))
            visited.add(rope[-1])

    return len(visited)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
