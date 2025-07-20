
import pytest
from solutions.solution_78 import is_interleave

@pytest.mark.parametrize("s1, s2, s3, expected", [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("a", "b", "ab", True),
    ("a", "b", "ba", True),
    ("ab", "a", "aba", True),
    ("ab", "a", "aab", True),
    ("a", "ab", "aab", True),
    ("a", "ab", "aba", True),
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "a", False),
    ("a", "", "a", True),
    ("", "a", "a", True),
    ("a", "b", "ac", False),
    ("a", "b", "ca", False),
    ("ab", "cd", "abcd", True),
    ("ab", "cd", "acbd", True),
    ("ab", "cd", "cdab", True),
    ("ab", "cd", "cadb", True)
])
def test_is_interleave(s1, s2, s3, expected):
    assert is_interleave(s1, s2, s3) == expected
