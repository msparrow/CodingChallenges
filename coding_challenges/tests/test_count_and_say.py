
import pytest
from solutions.solution_26 import count_and_say

@pytest.mark.parametrize("n, expected", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
    (5, "111221"),
    (6, "312211"),
    (7, "13112221"),
    (8, "1113213211"),
    (9, "31131211131221"),
    (10, "13211311123113112211")
])
def test_count_and_say(n, expected):
    assert count_and_say(n) == expected
