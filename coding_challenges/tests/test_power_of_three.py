
import pytest
from solutions.solution_149 import isPowerOfThree

test_cases = [
    (1, True),
    (3, True),
    (9, True),
    (27, True),
    (81, True),
    (243, True),
    (729, True),
    (2187, True),
    (6561, True),
    (19683, True),
    (59049, True),
    (177147, True),
    (531441, True),
    (1594323, True),
    (4782969, True),
    (14348907, True),
    (43046721, True),
    (129140163, True),
    (387420489, True),
    (1162261467, True),
    (0, False),
    (2, False),
    (4, False),
    (5, False),
    (6, False),
    (7, False),
    (8, False),
    (10, False),
    (11, False),
    (12, False),
    (13, False),
    (14, False),
    (15, False),
    (16, False),
    (20, False),
    (21, False),
    (22, False),
    (23, False),
    (24, False),
    (25, False),
    (26, False),
    (28, False),
    (29, False),
    (30, False),
    (31, False),
    (32, False),
    (100, False),
    (-1, False),
    (-3, False),
    (-9, False),
    (1162261468, False), #Slightly larger than the largest power of 3 representable as a 32-bit integer
    (float('inf'), False), # Test with infinity
    (float('-inf'), False), # Test with negative infinity
    (float('nan'), False) #Test with NaN

]


@pytest.mark.parametrize("n, expected", test_cases)
def test_isPowerOfThree(n, expected):
    assert isPowerOfThree(n) == expected

