import pytest
from solutions.solution_43 import merge

@pytest.mark.parametrize("intervals, expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 10], [2, 3], [4, 5], [6, 7]], [[1, 10]])
])
def test_merge(intervals, expected):
    assert merge(intervals) == expected