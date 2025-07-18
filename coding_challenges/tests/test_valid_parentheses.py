
import pytest
from solutions.solution_15 import is_valid

@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("", True),
    ("[", False),
    ("]", False),
    ("(((", False),
    (")))", False),
    ("((()))", True),
    ("((())])", False)
])
def test_is_valid(s, expected):
    assert is_valid(s) == expected
