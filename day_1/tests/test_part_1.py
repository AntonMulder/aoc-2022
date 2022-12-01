import pytest

from day_1.part_1 import run
from utils.io import read


@pytest.mark.parametrize(
    "test_input, expected",
    [(read("data/example_1.txt"), 24000)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
