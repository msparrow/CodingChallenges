
import pytest
from solutions.solution_72 import num_decodings

@pytest.mark.parametrize("s, expected", [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("06", 0),
    ("10", 1),
    ("27", 1)
])
def test_num_decodings(s, expected):
    assert num_decodings(s) == expected
