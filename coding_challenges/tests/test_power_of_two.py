
import pytest
from solutions.solution_148 import is_power_of_two_bitwise as is_power_of_two

# Test cases for is_power_of_two function

test_cases = [
    (1, True),
    (2, True),
    (4, True),
    (8, True),
    (16, True),
    (32, True),
    (64, True),
    (128, True),
    (256, True),
    (512, True),
    (1024, True),
    (2048, True),
    (4096, True),
    (8192, True),
    (16384, True),
    (32768, True),
    (65536, True),
    (131072, True),
    (262144, True),
    (524288, True),
    (1048576, True),
    (0, False),
    (3, False),
    (5, False),
    (6, False),
    (7, False),
    (9, False),
    (10, False),
    (15, False),
    (20, False),
    (21, False),
    (-1, False),
    (-2, False),
    (-4, False),
    (-8, False),
    (2**30, True),
    (2**31, True), #Edge case: large power of 2 within int range
    (2**31 -1, False), #Edge Case: number just below power of 2
    (2**31 + 1, False), #Edge Case: number just above power of 2
    (2**60, True), #another large power of 2
    (1073741824, True), # 2^30
    (-1073741824, False), #negative power of 2
    (1073741825,False), #number just above power of 2
    (1073741823,False), #number just below power of 2

    #Some random numbers
    (12345, False),
    (987654321, False),
    (1000000000, False),
    (111111111, False),
    (777777777, False),
    (1000, False),
    (3456, False),
    (1, True), #redundant but good for clarity
    (float('inf'),False), #Handles infinity
    (float('-inf'), False), #Handles negative infinity
    (float('nan'), False) #Handles NaN


]


@pytest.mark.parametrize("n, expected", test_cases)
def test_is_power_of_two(n, expected):
    assert is_power_of_two(n) == expected

