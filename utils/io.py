from typing import List


def read(path: str) -> str:
    with open(path) as f:
        data = f.read()
    return data


def read_lines(path: str) -> List[str]:
    with open(path) as f:
        data = f.readlines()
    return data
