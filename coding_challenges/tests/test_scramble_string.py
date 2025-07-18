
import pytest
from solutions.solution_68 import is_scramble

@pytest.mark.parametrize("s1, s2, expected", [
    ("great", "rgeat", True),
    ("abcde", "caebd", False),
    ("a", "a", True),
    ("a", "b", False),
    ("ab", "ba", True),
    ("abc", "bca", True)
])
def test_is_scramble(s1, s2, expected):
    assert is_scramble(s1, s2) == expected
