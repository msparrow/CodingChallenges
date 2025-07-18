
import pytest
from solutions.solution_23 import str_str

@pytest.mark.parametrize("haystack, needle, expected", [
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("", "", 0),
    ("a", "a", 0),
    ("mississippi", "issip", 4),
    ("mississippi", "pi", 9)
])
def test_str_str(haystack, needle, expected):
    assert str_str(haystack, needle) == expected
