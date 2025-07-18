
import pytest
from solutions.solution_69 import merge_sorted_array

@pytest.mark.parametrize("nums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1])
])
def test_merge_sorted_array(nums1, m, nums2, n, expected):
    merge_sorted_array(nums1, m, nums2, n)
    assert nums1 == expected
