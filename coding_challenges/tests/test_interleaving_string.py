
import pytest
from solutions.solution_78 import is_interleave

@pytest.mark.parametrize("s1, s2, s3, expected", [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True)
])
def test_is_interleave(s1, s2, s3, expected):
    assert is_interleave(s1, s2, s3) == expected
