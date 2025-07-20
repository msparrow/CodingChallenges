import pytest
from solutions.solution_45 import length_of_last_word

@pytest.mark.parametrize("s, expected", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("a", 1),
    (" a", 1),
    ("a ", 1),
    ("hello", 5),
    (" hello ", 5),
    ("", 0),
    ("a b c", 1),
    ("a b c ", 1),
    ("  a b c  ", 1),
    ("  a   b   c  ", 1),
    ("  hello world  ", 5),
    ("  hello   world  ", 5),
    ("  hello world   ", 5),
    ("  hello   world   ", 5),
    ("  hello world  \n", 5),
    ("\n  hello world  ", 5),
    ("  hello\nworld  ", 5)
])
def test_length_of_last_word(s, expected):
    assert length_of_last_word(s) == expected