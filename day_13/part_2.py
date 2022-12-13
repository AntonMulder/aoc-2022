from functools import cmp_to_key

from utils.io import read

ORDERED = 1
UNORDERED = -1
TBD = 0


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
    packets = []

    for index, pair in enumerate(puzzle_input.split("\n\n"), start=1):
        left, right = pair.split("\n")
        left = eval(left)
        packets.append(left)
        right = eval(right)
        packets.append(right)
    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=cmp_to_key(lambda x, y: compare_packet(x, y)))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
