
import pytest
from solutions.solution_103 import my_atoi

@pytest.mark.parametrize("s, expected", [
    ("42", 42),
    ("   -42", -42),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("", 0),
    ("+", 0),
    ("-", 0),
    ("  -0012a7", -12)
])
def test_my_atoi(s, expected):
    assert my_atoi(s) == expected
