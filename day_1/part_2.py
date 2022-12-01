from utils.io import read


def run(puzzle_input):
    per_elf = (x.split("\n") for x in puzzle_input.split("\n\n"))
    calories_per_elf = map(lambda elf: sum(int(x) for x in elf), per_elf)

    return sum(sorted(calories_per_elf)[-3:])


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
