from typing import Any, List, Set

from utils.io import readlines


def chunks(lst: List, n: int) -> Set[Any]:
    for i in range(0, len(lst), n):
        yield set(lst[i : i + n])


def run(puzzle_input):
    splitted_rucksacks = chunks(list(puzzle_input), 3)
    splitted_rucksacks_sets = ((map(set, x)) for x in splitted_rucksacks)
    splitted_rucksacks_intersection = (set.intersection(*x) for x in splitted_rucksacks_sets)
    chars = (next(iter(x)) for x in splitted_rucksacks_intersection)
    values = (ord(x) - 38 if x.upper() == x else ord(x) - 96 for x in chars)

    return sum(values)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
