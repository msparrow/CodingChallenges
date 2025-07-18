
import pytest
from solutions.solution_107 import roman_to_int

@pytest.mark.parametrize("s, expected", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("I", 1),
    ("IV", 4),
    ("IX", 9),
    ("X", 10),
    ("XL", 40),
    ("XC", 90),
    ("C", 100),
    ("CD", 400),
    ("CM", 900),
    ("D", 500),
    ("M", 1000)
])
def test_roman_to_int(s, expected):
    assert roman_to_int(s) == expected
