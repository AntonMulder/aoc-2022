from collections import deque

from utils.io import readlines
from utils.point import DIRECTIONS, Point


def run(puzzle_input):
    original_map = [line for line in puzzle_input]
    rows = len(original_map)
    columns = len(original_map[0])
    height_map = [[0 for _ in range(columns)] for _ in range(rows)]

    # Breath first search.
    queue = deque()
    for row in range(len(original_map)):
        for column in range(len(original_map[0])):
            x = original_map[row][column]
            if x == "S" or x == "a":
                queue.append((Point(row, column), 0))
                height_map[row][column] = 1
            elif x == "E":
                end = Point(row, column)
                height_map[row][column] = 26
            else:
                height_map[row][column] = ord(original_map[row][column]) - 96

    visited = set()
    while queue:
        p, distance = queue.popleft()
        if p in visited:
            continue
        visited.add(p)
        if p == end:
            return distance

        current_height = height_map[p.y][p.x]
        for direction in DIRECTIONS:
            possible_step = p + direction
            if 0 <= possible_step.x < columns and 0 <= possible_step.y < rows:
                new_height = height_map[possible_step.y][possible_step.x]
                if new_height <= 1 + current_height:
                    queue.append((possible_step, distance + 1))


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
