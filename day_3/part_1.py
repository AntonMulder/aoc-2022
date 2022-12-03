from utils.io import readlines


def run(puzzle_input):
    splitted_rucksacks = ((x[: len(x) // 2], x[len(x) // 2 :]) for x in puzzle_input)
    splitted_rucksacks_sets = ((map(set, x)) for x in splitted_rucksacks)
    splitted_rucksacks_intersection = (set.intersection(*x) for x in splitted_rucksacks_sets)
    chars = (x.pop() for x in splitted_rucksacks_intersection)
    values = (ord(x) - 38 if x.upper() == x else ord(x) - 96 for x in chars)

    return sum(values)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
