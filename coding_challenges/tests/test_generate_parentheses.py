
import pytest
from solutions.solution_17 import generate_parenthesis

@pytest.mark.parametrize("n, expected", [
    (3, sorted(["((()))","(()())","(())()","()(())","()()()"])),
    (1, sorted(["()"])),
    (2, sorted(["(())_()()"])),
    (4, sorted(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]))
])
def test_generate_parenthesis(n, expected):
    assert sorted(generate_parenthesis(n)) == expected
