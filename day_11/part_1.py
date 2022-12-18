import math
import re
from functools import reduce

from day_11.monkey import Monkey
from utils.io import read


def run(puzzle_input):
    monkeys = []
    for raw_monkey in puzzle_input.split("\n\n"):
        raw_monkey_line = raw_monkey.split("\n")
        id = re.search(r"\d+", raw_monkey_line[0])[0]
        starting_items = [int(x) for x in re.findall(r"\d+", raw_monkey_line[1])]
        operation = re.search(r"Operation: new = (.+)", raw_monkey_line[2]).groups()[0]
        divisible = int(re.search(r"\d+", raw_monkey_line[3])[0])
        if_true = int(re.search(r"\d+", raw_monkey_line[4])[0])
        if_false = int(re.search(r"\d+", raw_monkey_line[5])[0])

        monkey = Monkey(id, starting_items, operation, divisible, if_true, if_false)
        monkeys.append(monkey)

    for round in range(0, 20):
        for monkey in monkeys:
            # Get item one by one.
            while monkey.items:
                monkey.inspected += 1
                item = monkey.items.pop(0)

                new_worry = monkey.new_worry_level(item)
                new_worry_bored = math.floor(new_worry / 3)

                if new_worry_bored % monkey.divisible == 0:
                    monkeys[monkey.if_true].items.append(new_worry_bored)
                else:
                    monkeys[monkey.if_false].items.append(new_worry_bored)

    values = sorted([monkey.inspected for monkey in monkeys])[-2:]
    return reduce((lambda x, y: x * y), values)


if __name__ == "__main__":
    print(run(read("data/puzzle_input.txt")))
