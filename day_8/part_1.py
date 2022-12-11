from utils.io import readlines


def run(puzzle_input):
    trees = [[int(y) for y in x] for x in puzzle_input]

    total = 0
    for x in range(0, len(trees)):
        for y in range(0, len(trees)):

            if (x == 0 or x == len(trees) - 1) or (y == 0 or y == len(trees) - 1):
                total += 1
            else:
                tree = trees[y][x]
                if all((x < tree for x in trees[y][0:x])) or all((x < tree for x in trees[y][x + 1 :])):
                    total += 1
                    # Horizontal
                else:
                    # Vertical
                    column = [trees[t][x] for t in range(len(trees))]
                    if all((x < tree for x in column[0:y])) or all((x < tree for x in column[y + 1 :])):
                        print(tree)
                        total += 1

    return total


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
