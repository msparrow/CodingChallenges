
import pytest
from solutions.solution_130 import missingNumber_sum as missing_number

pytest_plugins = ['pytester']


def test_missing_number_empty_list():
    assert missing_number([]) == 0


def test_missing_number_single_element():
    assert missing_number([1]) == 0
    assert missing_number([0]) == 1


def test_missing_number_consecutive_numbers():
    assert missing_number([1, 2, 3, 4]) == 0
    assert missing_number([0, 1, 2, 3]) == 4
    assert missing_number([1, 2, 3, 4, 5]) == 0
    assert missing_number([0, 1, 2, 3, 4]) == 5


def test_missing_number_with_gaps():
    assert missing_number([0, 1, 3]) == 2
    assert missing_number([0, 2, 3]) == 1
    assert missing_number([1, 2, 4]) == 3
    assert missing_number([1, 3, 4]) == 2
    assert missing_number([0, 1, 2, 4, 5]) == 3
    assert missing_number([0, 1, 2, 3, 5]) == 4


def test_missing_number_large_list():
    nums = list(range(1000))
    nums.pop(500)
    assert missing_number(nums) == 500


def test_missing_number_negative_numbers():
    assert missing_number([-2, -1, 0, 1]) == 2
    assert missing_number([-2, -1, 1, 2]) == 0
    assert missing_number([-1, 0, 1, 2]) == -2


def test_missing_number_duplicate_numbers():
    assert missing_number([1, 2, 2, 3, 4]) == 0  #Assumes 0 as missing if duplicates exist
    assert missing_number([0,1,1,2,3]) == 4 #Assumes end of sequence if duplicates exist


def test_missing_number_unsorted_list():
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([2, 1, 0]) == 3
    assert missing_number([4, 1, 3, 2]) == 0
    assert missing_number([1, 4, 3, 0]) == 2


# Additional test cases for edge cases and boundary conditions

def test_missing_number_all_zeros():
    assert missing_number([0, 0, 0, 0]) == 1 #assumes 1 is missing

def test_missing_number_all_ones():
    assert missing_number([1,1,1,1]) == 0 # assumes 0 is missing

def test_missing_number_large_range():
    nums = list(range(10000))
    nums.pop(7500)
    assert missing_number(nums) == 7500

def test_missing_number_negative_range():
    nums = list(range(-100,0))
    nums.pop(-50)
    assert missing_number(nums) == -50


# Test cases with various input sizes

test_data = [
    ([], 0),
    ([1], 0),
    ([0], 1),
    ([1,2,3],0),
    ([0,1,2],3),
    ([0,1,3],2),
    ([1,2,4],3),
    ([1,3,4],2),
    ([2,3,4],1),
    ([1,2,3,4,5,6,7,8,9],0),
    ([0,2,1,3],4),
    ([4,3,1,2,0],5),
    (list(range(100)),100),
    (list(range(0,100)),100),
    (list(range(-50,50)),50), #Includes negatives
    (list(range(-100,-50)),-50),
    ([1, 3, 0, 2, 6, 4, 5], 7),
    ([0,1,2,3,4,5,6,7,9],8),
    ([9,8,7,6,5,4,3,2,1,0], 10),
    (list(range(1000))[:-1], 999),
    ([0, 2, 1],3)

]



@pytest.mark.parametrize("input_list, expected_output", test_data)
def test_missing_number_param(input_list, expected_output):
    assert missing_number(input_list) == expected_output
