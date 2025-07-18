
import pytest
from solutions.solution_27 import combination_sum

@pytest.mark.parametrize("candidates, target, expected", [
    ([2, 3, 6, 7], 7, sorted([[2, 2, 3], [7]])),
    ([2, 3, 5], 8, sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])),
    ([2], 1, []),
    ([1], 1, [[1]]),
    ([1], 2, [[1, 1]])
])
def test_combination_sum(candidates, target, expected):
    result = combination_sum(candidates, target)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
