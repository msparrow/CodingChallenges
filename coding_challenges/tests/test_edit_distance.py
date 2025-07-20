
import pytest
from solutions.solution_52 import min_distance

@pytest.mark.parametrize("word1, word2, expected", [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "", 0),
    ("a", "b", 1),
    ("a", "", 1),
    ("", "a", 1),
    ("a", "", 1),
    ("ab", "ac", 1),
    ("ab", "ba", 2),
    ("saturday", "sunday", 3),
    ("cat", "cut", 1),
    ("girl", "grill", 2),
    ("python", "pythons", 1),
    ("apple", "apply", 1),
    ("banana", "bandana", 1),
    ("sea", "eat", 2),
    ("teacher", "preacher", 2),
    ("algorithm", "logarithm", 2),
    ("computer", "commuter", 1),
    ("abcdef", "azced", 2)
])
def test_min_distance(word1, word2, expected):
    assert min_distance(word1, word2) == expected
