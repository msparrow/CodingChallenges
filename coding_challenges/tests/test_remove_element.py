
import pytest
from solutions.solution_22 import remove_element

@pytest.mark.parametrize("nums, val, expected_k, expected_nums", [
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
    ([], 0, 0, []),
    ([1, 1, 1], 1, 0, []),
    ([1, 2, 3], 4, 3, [1, 2, 3]),
    ([1, 1, 2, 2, 3, 3], 1, 4, [2, 2, 3, 3]),
    ([1, 2, 3, 4, 5], 6, 5, [1, 2, 3, 4, 5]),
    ([1, 1, 1, 1, 1], 1, 0, []),
    ([1, 2, 3, 4, 5], 3, 4, [1, 2, 4, 5]),
    ([-1, 0, 1, 2, 3], 0, 4, [-1, 1, 2, 3]),
    ([1, 1, 2, 2, 3, 3], 2, 4, [1, 1, 3, 3]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 9, [1, 2, 3, 4, 6, 7, 8, 9, 10]),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0, []),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2], 1, 1, [2]),
    ([1, 2, 1, 2, 1, 2, 1, 2], 1, 4, [2, 2, 2, 2]),
    ([1, 2, 3, 4, 5], 1, 4, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 5, 4, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 3, 4, [1, 2, 4, 5]),
    ([1, 2, 3, 4, 5], 2, 4, [1, 3, 4, 5])
])
def test_remove_element(nums, val, expected_k, expected_nums):
    k = remove_element(nums, val)
    assert k == expected_k
    # The problem statement says the order of the elements may be changed.
    # So we sort both lists before comparing them.
    assert sorted(nums[:k]) == sorted(expected_nums)
