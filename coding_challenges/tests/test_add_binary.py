import pytest
from solutions.solution_47 import add_binary

@pytest.mark.parametrize("a, b, expected", [
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
    ("0", "0", "0"),
    ("1", "1", "10"),
    ("1111", "1111", "11110")
])
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected