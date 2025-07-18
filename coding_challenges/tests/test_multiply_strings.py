
import pytest
from solutions.solution_31 import multiply

@pytest.mark.parametrize("num1, num2, expected", [
    ("2", "3", "6"),
    ("123", "456", "56088"),
    ("0", "0", "0"),
    ("9", "9", "81"),
    ("99", "99", "9801"),
    ("100", "100", "10000")
])
def test_multiply(num1, num2, expected):
    assert multiply(num1, num2) == expected
