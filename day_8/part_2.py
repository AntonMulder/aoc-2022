from utils.io import readlines


def run(puzzle_input):
    trees = [[int(y) for y in x] for x in puzzle_input]

    max_distance = 0

    for x in range(1, len(trees) - 1):
        column = [trees[t][x] for t in range(len(trees))]
        for y in range(1, len(trees) - 1):
            tree = trees[y][x]
            row = trees[y]
            total_distance = 1

            # Up
            distance = 0
            for up_y in range(y - 1, -1, -1):
                distance += 1
                if column[up_y] >= tree:
                    break
            total_distance *= distance

            # Right
            distance = 0
            for right_x in range(x + 1, len(trees)):
                distance += 1
                if row[right_x] >= tree:
                    break
            total_distance *= distance

            # Down
            distance = 0
            for down_y in range(y + 1, len(trees)):
                distance += 1
                if column[down_y] >= tree:
                    break
            total_distance *= distance

            # Left
            distance = 0
            for left_x in range(x - 1, -1, -1):
                distance += 1
                if row[left_x] >= tree:
                    break
            total_distance *= distance

            max_distance = max(max_distance, total_distance)

    return max_distance


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
