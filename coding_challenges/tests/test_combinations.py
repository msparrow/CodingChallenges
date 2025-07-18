import pytest
from solutions.solution_56 import combine

@pytest.mark.parametrize("n, k, expected", [
    (4, 2, sorted([[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])),
    (1, 1, [[1]]),
    (4, 1, [[1], [2], [3], [4]]),
    (4, 4, [[1, 2, 3, 4]])
])
def test_combine(n, k, expected):
    result = combine(n, k)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])