import pytest
from solutions.solution_55 import min_window

@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ab", "a", "a"),
    ("ab", "b", "b"),
    ("abc", "c", "c")
])
def test_min_window(s, t, expected):
    assert min_window(s, t) == expected