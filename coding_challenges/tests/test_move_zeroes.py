
import pytest
from solutions.solution_129 import move_zeroes  # Assuming your solution is in this file

def test_move_zeroes_empty_list():
    nums = []
    move_zeroes(nums)
    assert nums == []

def test_move_zeroes_all_zeros():
    nums = [0, 0, 0]
    move_zeroes(nums)
    assert nums == [0, 0, 0]

def test_move_zeroes_all_non_zeros():
    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3]

def test_move_zeroes_single_zero():
    nums = [1, 0, 2]
    move_zeroes(nums)
    assert nums == [1, 2, 0]

def test_move_zeroes_multiple_zeros():
    nums = [1, 0, 2, 0, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0]

def test_move_zeroes_zeros_at_beginning():
    nums = [0, 1, 0, 2, 0, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

def test_move_zeroes_zeros_at_end():
    nums = [1, 2, 3, 0, 0, 0]
    move_zeroes(nums)
    assert nums == [1, 2, 3, 0, 0, 0]

def test_move_zeroes_negative_numbers():
    nums = [-1, 0, -2, 0, -3]
    move_zeroes(nums)
    assert nums == [-1, -2, -3, 0, 0]

def test_move_zeroes_mixed_numbers():
    nums = [-1, 0, 2, 0, -3, 0, 4]
    move_zeroes(nums)
    assert nums == [-1, 2, -3, 4, 0, 0, 0]

def test_move_zeroes_large_list():
    nums = list(range(100))
    nums[25] = 0
    nums[50] = 0
    nums[75] = 0
    expected = [x for x in nums if x != 0] + [0] * 3
    move_zeroes(nums)
    assert nums == expected


# More test cases for better coverage:

@pytest.mark.parametrize("nums, expected", [
    ([0], [0]),
    ([1,0], [1,0]),
    ([0,1], [1,0]),
    ([1,0,0], [1,0,0]),
    ([0,0,1], [1,0,0]),
    ([0,1,0], [1,0,0]),
    ([1,0,1,0], [1,1,0,0]),
    ([0,1,0,1], [1,1,0,0]),
    ([1,1,1,0,0,0], [1,1,1,0,0,0]),
    ([0,0,0,1,1,1], [1,1,1,0,0,0]),
    ([1,2,3,4,5,0], [1,2,3,4,5,0]),
    ([0,1,2,3,4,5], [1,2,3,4,5,0]),
    ([1, 0, 1, 0, 1, 0,1], [1, 1, 1, 1, 0, 0, 0]),
    ([1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 0]),
    ([-1, 0, -2, 0, -3, 0], [-1, -2, -3, 0, 0, 0]),
    ([1, 2, 0, 0, 0, 3, 4, 5, 0, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]),
    ([1, 2, 3, 4, 5, 0, 0, 0, 0, 0], [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]),
    ([0, 0, 0, 0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 0, 0, 0, 0]),
    ([1, 2, 3, 4, 5, 0, 0, 0, 1, 0], [1, 2, 3, 4, 5, 1, 0, 0, 0, 0]),

])
def test_move_zeroes_parametrized(nums, expected):
    move_zeroes(nums)
    assert nums == expected


#Add more test cases as needed to cover edge cases and various scenarios.  The more the merrier