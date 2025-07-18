
import pytest
from solutions.solution_21 import remove_duplicates

@pytest.mark.parametrize("nums, expected_k, expected_nums", [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ([], 0, []),
    ([1, 1, 1], 1, [1]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([1, 1, 2, 2, 3, 3], 3, [1, 2, 3])
])
def test_remove_duplicates(nums, expected_k, expected_nums):
    k = remove_duplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_nums
