
import pytest
from solutions.solution_122 import containsDuplicate

# Test cases for containsDuplicate function

test_cases = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([], False),
    ([1], False),
    ([1,1,1,1,1,1,1,1,1,1], True),
    ([0,0,0,0,0,0,0,0,0,0], True),
    ([-1,-1,-1,-1,-1], True),
    ([1,2,3,4,5,6,7,8,9,10], False),
    ([10,9,8,7,6,5,4,3,2,1], False),
    ([1,2,3,4,5,6,7,8,9,10,1], True),
    ([10,9,8,7,6,5,4,3,2,1,10], True),
    ([1, 1, 1, 2, 2, 2, 3, 3, 3], True),
    ([1, 2, 3, 4, 5, 1], True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], False),
    ([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], False),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], True),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1],True),
    (list(range(100)), False),
    (list(range(100)) + [50], True),
    (list(range(1000)), False),
    (list(range(1000)) + [500], True),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5], True),
    ([1] * 100, True),
    ([0] * 1000, True),
    ([-1] * 50, True),
    ([1, -1, 2, -2, 3, -3], False),
    ([1, -1, 2, -2, 3, -3, 1], True),
    ([float('nan'), float('nan')], True), #Test for NaN
    ([float('inf'), float('-inf')], False), #Test for infinity
    ([float('inf'), float('inf')], True), # Test for infinity duplicates
    ([1, 2, 3, 4, 5, float('nan')], True), #Test NaN with other numbers.
    ([1, 2, 3, 4, 5, float('inf')], True), #Test Infinity with other numbers.
    ([], False),
    ([None], False),
    ([None, None], True),
    ([1, None, 2, None], True),
    ([None, 1, None, 2], True),
    ([1,2,3,4,5,"a"], False),
    ([1,2,3,4,5,"a","a"], True),
    (["a","b","c","d","a"],True),
    (["apple", "banana", "apple"], True),
    (["apple", "banana", "orange"], False),
    ([True, False, True], True),
    ([True, False, False], False),
    ([1, 2, 3, 4, 5, 1.0], True), # Test for integer and float with same value
    ([1, 2, 3, 4, 5, 1.1], False), # Test for integer and float with different value
    ([1, 2, 3, 4, 5, "1"], True), # Test for integer and string representation of the integer
    ([1, 2, 3, 4, 5, "1.0"], True), # Test for integer and string representation of a float
    ([1,2,3,4,5, 1+0j], True), #Test for complex number
    ([1,2,3,4,5, 1+1j], False), #Test for complex number
    ([1,2,3,4,5, "1+0j"], True), #Test string complex number


]


@pytest.mark.parametrize("input_list, expected", test_cases)
def test_containsDuplicate(input_list, expected):
    assert containsDuplicate(input_list) == expected
