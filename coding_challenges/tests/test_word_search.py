import pytest
from solutions.solution_58 import exist

@pytest.mark.parametrize("board, word, expected", [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ([["a"]], "a", True)
])
def test_exist(board, word, expected):
    assert exist(board, word) == expected