from typing import List


def read(path: str) -> str:
    with open(path) as f:
        data = f.read()
    return data


def readlines(path: str) -> List[str]:
    with open(path) as f:
        data = f.readlines()
    return data
