
import pytest
from solutions.solution_23 import str_str

@pytest.mark.parametrize("haystack, needle, expected", [
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("", "", 0),
    ("a", "a", 0),
    ("mississippi", "issip", 4),
    ("mississippi", "pi", 9),
    ("a", "", 0),
    ("", "a", -1),
    ("abc", "abc", 0),
    ("abc", "b", 1),
    ("abc", "d", -1),
    ("aaaaa", "a", 0),
    ("aaaaa", "aaaaa", 0),
    ("mississippi", "mississippi", 0),
    ("mississippi", "issipp", 4),
    ("mississippi", "sippia", -1),
    ("b", "a", -1),
    ("b", "b", 0),
    ("b", "", 0)
])
def test_str_str(haystack, needle, expected):
    assert str_str(haystack, needle) == expected
