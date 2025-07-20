
import pytest
from solutions.solution_72 import num_decodings

@pytest.mark.parametrize("s, expected", [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("06", 0),
    ("10", 1),
    ("27", 1),
    ("1111", 5),
    ("1212", 5),
    ("1234", 3),
    ("2626", 4),
    ("1010", 1),
    ("1001", 0),
    ("2222", 5),
    ("3333", 1),
    ("12321", 6),
    ("11111", 8),
    ("111111", 13),
    ("1111111", 21),
    ("11111111", 34),
    ("111111111", 55)
])
def test_num_decodings(s, expected):
    assert num_decodings(s) == expected
