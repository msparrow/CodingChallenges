import pytest
from solutions.solution_45 import length_of_last_word

@pytest.mark.parametrize("s, expected", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("a", 1),
    (" a", 1),
    ("a ", 1)
])
def test_length_of_last_word(s, expected):
    assert length_of_last_word(s) == expected