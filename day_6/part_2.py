from utils.io import read


def run(puzzle_input):
    index = 0
    while True:
        sequenze = puzzle_input[index - 14 : index]
        if len(set(sequenze)) == 14:
            break
        index += 1

    return index


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
