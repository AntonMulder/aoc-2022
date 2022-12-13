from utils.io import read

ORDERED = 1
UNORDERED = 2
TBD = 3


def compare_packet(left, right):
    # Check if integers are the same.
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return UNORDERED
        elif left > right:
            return ORDERED
        return TBD
    # Check both items are lists
    elif isinstance(left, list) and isinstance(right, list):
        index = 0
        for sub_left, sub_right in zip(left, right):
            result = compare_packet(sub_left, sub_right)
            if result != TBD:
                return result
            index += 1

        if len(left) < len(right):
            return UNORDERED
        elif index == len(right) and index < len(left):
            return ORDERED
        return TBD
    # Either one of them is a list, so convert the other one.
    elif isinstance(left, int) and isinstance(right, list):
        return compare_packet([left], right)
    return compare_packet(left, [right])


def run(puzzle_input):
    result = 0
    for index, pair in enumerate(puzzle_input.split("\n\n"), start=1):
        left, right = pair.split("\n")
        left = eval(left)
        right = eval(right)

        if compare_packet(left, right) == UNORDERED:
            result += index

    return result


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
