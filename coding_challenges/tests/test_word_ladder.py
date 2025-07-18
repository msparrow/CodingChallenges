
import pytest
from solutions.solution_100 import ladder_length

@pytest.mark.parametrize("begin_word, end_word, word_list, expected", [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
    ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
    ("a", "c", ["a","b","c"], 2)
])
def test_ladder_length(begin_word, end_word, word_list, expected):
    assert ladder_length(begin_word, end_word, word_list) == expected
