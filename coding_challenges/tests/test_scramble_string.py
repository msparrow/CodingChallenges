
import pytest
from solutions.solution_68 import is_scramble

@pytest.mark.parametrize("s1, s2, expected", [
    ("great", "rgeat", True),
    ("abcde", "caebd", False),
    ("a", "a", True),
    ("a", "b", False),
    ("ab", "ba", True),
    ("abc", "bca", True),
    ("abc", "acb", True),
    ("ab", "ab", True),
    ("great", "eatgr", True),
    ("p", "p", True),
    ("abcde", "edcba", True),
    ("abcdefghij", "efghijabcd", True),
    ("abcdefghij", "jighfedcba", True),
    ("a", "b", False),
    ("ab", "ca", False),
    ("abc", "adc", False),
    ("great", "rgeatx", False),
    ("great", "rgeatt", False),
    ("abcdefghij", "efghijabdc", False)
])
def test_is_scramble(s1, s2, expected):
    assert is_scramble(s1, s2) == expected
