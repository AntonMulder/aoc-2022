import pytest

from day_9.part_2 import run
from utils.io import readlines


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (readlines("data/example_1.txt"), 1),
        (readlines("data/example_2.txt"), 36),
    ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
