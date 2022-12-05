import re
from collections import deque

from utils.io import readlines

INSTRUCTION_RE = re.compile(r"move (\d+) from (\d+) to (\d)")


def run(puzzle_input):
    stacks = {
        "1": deque(["R", "G", "H", "Q", "S", "B", "T", "N"]),
        "2": deque(["H", "S", "F", "D", "P", "Z", "J"]),
        "3": deque(["Z", "H", "V"]),
        "4": deque(["M", "Z", "J", "F", "G", "H"]),
        "5": deque(["T", "Z", "C", "D", "L", "M", "S", "R"]),
        "6": deque(["M", "T", "W", "V", "H", "Z", "J"]),
        "7": deque(["T", "F", "P", "L", "Z"]),
        "8": deque(["Q", "V", "W", "S"]),
        "9": deque(["W", "H", "L", "M", "T", "D", "N", "C"]),
    }

    for instruction in puzzle_input:
        amount, location, target = INSTRUCTION_RE.match(instruction).groups()

        picked = reversed([stacks[location].pop() for _ in range(int(amount))])

        stacks[target].extend(picked)

    return "".join([stacks[stack].pop() for stack in stacks])


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
