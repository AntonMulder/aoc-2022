import pytest

from day_6.part_2 import run


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
