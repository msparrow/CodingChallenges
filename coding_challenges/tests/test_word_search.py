import pytest
from solutions.solution_58 import exist

@pytest.mark.parametrize("board, word, expected", [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ([["a"]], "a", True),
    ([["a"]], "b", False),
    ([["a","b"],["c","d"]], "abcd", False),
    ([["a","b"],["c","d"]], "acdb", True),
    ([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS", True),
    ([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ASADFBCCEESE", True),
    ([["a","a"]], "aaa", False),
    ([["a","b"],["c","d"]], "abdc", True),
    ([["a","b"],["c","d"]], "acbd", True),
    ([["a","b","c"],["d","e","f"],["g","h","i"]], "abcfi", True),
    ([["a","b","c"],["d","e","f"],["g","h","i"]], "ihgdebca", True),
    ([["a","b","c"],["d","e","f"],["g","h","i"]], "adghebcfi", True),
    ([["a","b","c"],["d","e","f"],["g","h","i"]], "abcdefi", False),
    ([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaa", True),
    ([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaab", False),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SFCSEEDA", True)
])
def test_exist(board, word, expected):
    assert exist(board, word) == expected