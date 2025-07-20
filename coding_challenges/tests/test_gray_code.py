
import pytest
from solutions.solution_70 import gray_code

@pytest.mark.parametrize("n, expected", [
    (2, [0, 1, 3, 2]),
    (1, [0, 1]),
    (3, [0, 1, 3, 2, 6, 7, 5, 4]),
    (4, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]),
    (5, [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16]),
    (0, [0])
])
def test_gray_code(n, expected):
    assert gray_code(n) == expected
