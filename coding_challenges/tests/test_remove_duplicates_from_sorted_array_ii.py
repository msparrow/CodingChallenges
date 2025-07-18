import pytest
from solutions.solution_64 import remove_duplicates2

@pytest.mark.parametrize("nums, expected_k, expected_nums", [
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ([1, 1, 1, 1, 1], 2, [1, 1])
])
def test_remove_duplicates2(nums, expected_k, expected_nums):
    k = remove_duplicates2(nums)
    assert k == expected_k
    assert nums[:k] == expected_nums