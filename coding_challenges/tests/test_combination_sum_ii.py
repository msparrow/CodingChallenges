
import pytest
from solutions.solution_28 import combination_sum2

@pytest.mark.parametrize("candidates, target, expected", [
    ([10, 1, 2, 7, 6, 1, 5], 8, sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])),
    ([2, 5, 2, 1, 2], 5, sorted([[1, 2, 2], [5]])),
    ([1, 1], 1, [[1]]),
    ([1, 1], 2, [[1, 1]])
])
def test_combination_sum2(candidates, target, expected):
    result = combination_sum2(candidates, target)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
