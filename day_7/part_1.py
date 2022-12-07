import re
from collections import defaultdict

from utils.io import readlines

CD_RE = re.compile(r"\$ cd (\w+)")
FILE_RE = re.compile(r"^(\d+) .+")


def run(puzzle_input):
    directory = []
    sizes = defaultdict(lambda: 0)

    for command in puzzle_input:
        if command == "$ cd /":
            directory = [""]
        elif command == "$ cd ..":
            directory.pop()
        elif cd := CD_RE.match(command):
            directory.append(cd.groups()[0])
        elif size := FILE_RE.match(command):
            temp_dir = ""
            for sub_directory in directory:
                temp_dir += sub_directory + "/"
                sizes[temp_dir] += int(size.groups()[0])

    return sum(filter(lambda x: x <= 100000, sizes.values()))


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
