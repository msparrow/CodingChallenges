
import pytest
from solutions.solution_52 import min_distance

@pytest.mark.parametrize("word1, word2, expected", [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "", 0),
    ("a", "b", 1),
    ("a", "", 1),
    ("", "a", 1)
])
def test_min_distance(word1, word2, expected):
    assert min_distance(word1, word2) == expected
