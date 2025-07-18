
import pytest
from solutions.solution_70 import gray_code

@pytest.mark.parametrize("n, expected", [
    (2, [0, 1, 3, 2]),
    (1, [0, 1]),
    (3, [0, 1, 3, 2, 6, 7, 5, 4])
])
def test_gray_code(n, expected):
    assert gray_code(n) == expected
