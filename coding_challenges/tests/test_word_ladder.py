
import pytest
from solutions.solution_100 import ladder_length

@pytest.mark.parametrize("begin_word, end_word, word_list, expected", [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
    ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
    ("a", "c", ["a","b","c"], 2),
    ("hot", "dog", ["hot","dog"], 0),
    ("hot", "dog", ["hot","dot","dog"], 3),
    ("leet", "code", ["lest","leet","lose","code","lode","robe","lost"], 6),
    ("teach", "place", ["peach","peace","place","reach","teach"], 4),
    ("apple", "banana", ["apply","bpple","baple","banle","banan","banana"], 7),
    ("cat", "dog", ["bat","cot","cog","dog"], 4),
    ("red", "blue", ["rad","rod","rid","red","bud","bad","bed","bid","blue"], 5),
    ("big", "cat", ["big","bit","bat","cat"], 4),
    ("warm", "cold", ["worm","ward","word","cord","cold"], 5),
    ("stone", "money", ["store","shone","phone","phoney","money"], 5),
    ("go", "no", ["go", "no"], 2),
    ("on", "in", ["on", "in"], 2),
    ("a", "b", ["a", "b"], 2),
    ("same", "same", ["same"], 1),
    ("talk", "tail", ["talk", "tall", "tail"], 3),
    ("head", "tail", ["heal","teal","tell","tall","tail"], 5),
    ("sand", "band", ["sand", "band"], 2)
])
def test_ladder_length(begin_word, end_word, word_list, expected):
    assert ladder_length(begin_word, end_word, word_list) == expected
