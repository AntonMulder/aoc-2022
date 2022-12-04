import re

from utils.io import readlines

PAIRS_RE = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def run(puzzle_input):
    pairs = (map(int, PAIRS_RE.match(x).groups()) for x in puzzle_input)

    def fully_contains(left_lower, left_upper, right_lower, right_upper):
        if (left_lower >= right_lower and left_upper <= right_upper) or (
            right_lower >= left_lower and right_upper <= left_upper
        ):
            return True

    result = filter(lambda x: fully_contains(*x), pairs)

    return sum(1 for _ in result)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
