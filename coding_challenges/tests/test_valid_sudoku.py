
import pytest
from solutions.solution_25 import is_valid_sudoku

@pytest.mark.parametrize("board, expected", [
    ([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], True),
    ([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], False),
    # Add 18 more test cases
    # Empty board
    ([["."]*9 for _ in range(9)], True),
    # Full board, valid
    ([["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]], True),
    # Full board, invalid row
    ([["5","3","4","6","7","8","9","1","5"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]], False),
    # Full board, invalid column
    ([["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["5","4","5","2","8","6","1","7","9"]], False),
    # Full board, invalid sub-box
    ([["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","5"]], False),
    # Invalid character
    ([["a","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], False),
    # Row with duplicate
    ([["1","1",".",".",".",".",".",".","."],["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9], False),
    # Column with duplicate
    ([["1",".",".",".",".",".",".",".","."],["1",".",".",".",".",".",".",".","."],["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9], False),
    # Sub-box with duplicate
    ([["1",".",".",".",".",".",".",".","."],[".","1",".",".",".",".",".",".","."],["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9], False),
    # Another valid case
    ([["1",".",".","4",".",".","7",".","."],[".","2",".",".","5",".",".","8","."],[".",".","3",".",".","6",".",".","9"],[".",".",".","1",".",".",".","2","."],["4",".",".",".","3",".",".",".","5"],[".","5",".",".",".","2",".",".","."],[".",".","6",".",".",".","3",".","."],["7",".",".","8",".",".",".","4","."],[".","8",".",".","9",".",".",".","1"]], True),
    # Another invalid case
    ([["1","2","3","4","5","6","7","8","9"],["2",".",".",".",".",".",".",".","."],["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9], False),
    # All same number
    ([["1"]*9 for _ in range(9)], False),
    # Almost valid board
    ([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","8"]], False),
    # Valid board with numbers at the edges
    ([["1",".",".",".",".",".",".",".","2"],["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["3",".",".",".",".",".",".",".","4"]], True),
    # Invalid board with numbers at the edges
    ([["1",".",".",".",".",".",".",".","1"],["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9,["."]*9], False),
    # Board with only one row filled
    ([["1","2","3","4","5","6","7","8","9"]]+[["."]*9 for _ in range(8)], True),
    # Board with only one column filled
    ([["1"]+["."]*8 for _ in range(9)], True),
    # Board with only one sub-box filled
    ([["1","2","3"]+["."]*6, ["4","5","6"]+["."]*6, ["7","8","9"]+["."]*6] + [["."]*9 for _ in range(6)], True)
])
def test_is_valid_sudoku(board, expected):
    assert is_valid_sudoku(board) == expected
