import re

from utils.io import readlines

INSTRUCTION_RE = re.compile(r"move (\d+) from (\d+) to (\d)")


def run(puzzle_input):
    stacks = {
        "1": ["R", "G", "H", "Q", "S", "B", "T", "N"],
        "2": ["H", "S", "F", "D", "P", "Z", "J"],
        "3": ["Z", "H", "V"],
        "4": ["M", "Z", "J", "F", "G", "H"],
        "5": ["T", "Z", "C", "D", "L", "M", "S", "R"],
        "6": ["M", "T", "W", "V", "H", "Z", "J"],
        "7": ["T", "F", "P", "L", "Z"],
        "8": ["Q", "V", "W", "S"],
        "9": ["W", "H", "L", "M", "T", "D", "N", "C"],
    }

    for instruction in puzzle_input:
        amount, location, target = INSTRUCTION_RE.match(instruction).groups()
        picked = (stacks[location].pop() for _ in range(int(amount)))
        stacks[target].extend(picked)

    return "".join([stacks[stack].pop() for stack in stacks])


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
