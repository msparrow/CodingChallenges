import pytest
from solutions.solution_55 import min_window

@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ab", "a", "a"),
    ("ab", "b", "b"),
    ("abc", "c", "c"),
    ("abc", "d", ""),
    ("adobecodebanc", "abc", "banc"),
    ("adobecodebanc", "abac", "banc"),
    ("cabwefgewcwaefgcf", "cae", "cwae"),
    ("a", "b", ""),
    ("ab", "A", ""),
    ("ADOBECODEBANC", "ABCZ", ""),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("bba", "ab", "ba"),
    ("acbbaca", "aba", "baca"),
    ("aaaaaaaaaaa", "a", "a"),
    ("aaaaaaaaaaa", "aa", "aa"),
    ("aaaaaaaaaaa", "aaa", "aaa")
])
def test_min_window(s, t, expected):
    assert min_window(s, t) == expected