from typing import List


class Monkey:
    def __init__(self, id: int, items: List[int], operation: str, divisible: int, if_true: int, if_false: int):
        self.id = id
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def new_worry_level(self, worry_level: int) -> int:
        _, operator, right = self.operation.split(" ")

        if right == "old":
            right = worry_level
        else:
            right = int(right)

        if operator == "+":
            return worry_level + right
        else:
            return worry_level * right

    def __str__(self) -> str:
        return f"Monkey {self.id}\nItems: {self.items}"
