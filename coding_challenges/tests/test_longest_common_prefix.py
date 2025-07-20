
import pytest
from solutions.solution_102 import longest_common_prefix

@pytest.mark.parametrize("strs, expected", [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
    (["a"], "a"),
    (["ab", "a"], "a"),
    (["", ""], ""),
    (["abc", "ab", "a"], "a"),
    (["apple", "apply", "ape"], "ap"),
    (["apple", "orange", "banana"], ""),
    (["a", "b", "c"], ""),
    (["aa", "ab"], "a"),
    (["abab", "aba", "abc"], "ab"),
    (["c", "c"], "c"),
    (["", "a"], ""),
    (["a", ""], ""),
    (["abab", "ab"], "ab"),
    (["flower", "flow", "flight", "fluent"], "fl"),
    (["a"], "a"),
    ([], ""),
    (["", ""], "")
])
def test_longest_common_prefix(strs, expected):
    assert longest_common_prefix(strs) == expected
