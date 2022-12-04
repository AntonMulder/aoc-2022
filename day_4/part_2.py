import re

from utils.io import readlines

PAIRS_RE = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def run(puzzle_input):
    pairs = (map(int, PAIRS_RE.match(x).groups()) for x in puzzle_input)

    def contains(left_lower, left_upper, right_lower, right_upper):
        if (
            right_lower <= left_lower <= right_upper
            or right_lower <= left_upper <= right_upper
            or left_lower <= right_lower <= left_upper
            or left_lower <= right_upper <= left_upper
        ):
            return True

    result = filter(lambda x: contains(*x), pairs)

    return sum(1 for _ in result)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
