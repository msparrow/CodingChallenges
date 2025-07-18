```python
import pytest
from solutions.solution_138 import isAnagram

# Test cases for Valid Anagram

test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("", "", True),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "bca", True),
    ("listen", "silent", True),
    ("elbow", "below", True),
    ("hello", "world", False),
    ("A man, a plan, a canal: Panama", "ama naplanacanalpanama", True), #ignoring case and spaces
    (" ", " ", True),
    ("a", "", False),
    ("", "a", False),
    ("ab", "abc", False),
    ("abc", "ab", False),
    ("123", "321", True),
    ("123", "3211", False),
    ("123", "1123", False),
    ("!", "!", True),
    ("!!", "!!", True),
    ("!!", "!!!", False),
    ("a!", "a", False),
    ("a!", "!a", True),
    ("A", "a", True),  # Case-insensitive
    ("Aa", "aA", True), # Case-insensitive
    ("AaBbCc", "cCbBaa", True), # Case-insensitive
    ("race a car", "raceacar", True), #ignoring spaces
    ("Race car", "Racecar", True), #Ignoring spaces and case
    ("パタトクカシーー", "シーーパタトクカ", True), #Japanese characters
    ("你好世界", "世界你好", True), #Chinese characters
    ("你好世界", "你好宇宙", False), #Chinese characters
    ("This is a test", "This is a Test", True), #Case insensitive
    ("This is a test!", "This is a test", False), #Punctuation matters
    ("This is a test.", "This.is a test", False), #Punctuation matters


    # Edge cases and boundary conditions
    (" ", "  ", False), #different number of spaces
    ("a", " a", False), #leading space
    (" a", "a", False), #trailing space
    ("\t", "\t", True), #tab character
    ("\n", "\n", True), #newline character
    ("a\n", "a", False), #newline matters
    ("a\t", "a", False), #tab matters

    #Long strings
    ("longstring"*10, ("longstring"*10)[::-1], True),
    ("longstring"*10 + "a", ("longstring"*10)[::-1], False),
    ("longstring"*10, ("longstring"*10)[::-1] + "a", False),


    #Repeated characters
    ("aaaa", "aaaa", True),
    ("aaabbbccc", "aaabbbccc", True),
    ("aaabbbccc", "aaabbcccb", True),
    ("aaabbbccc", "aabbbccca", False),


    #Mixed case and characters
    ("AbCdEfGhIjKlMnOpQrStUvWxYz", "zYxWvUtSrQpOnMlKjIhGfEdCbA", True),
    ("1A2b3c4d", "d4c3b2A1", True),


    #Numbers and Characters mixed
    ("1a2b3c", "c3b2a1", True),
    ("1a2b3c", "c3b2a2", False),
    ("1a2b3c", "c3b1a2", False),

    ("hello", "olleh", True),
    ("aacc", "ccaa", True),
    ("aabb", "baba", True),
    ("qwerty", "ytrewq", True),
    ("stressed", "desserts", True),
    ("cinema", "iceman", True),
    ("dormitory", "dirtyroom", True),
    ("admirer", "married", True),
    ("conversation", "voices rant on", True),
    ("Debit card", "bad credit", True),
    ("state", "taste", True),
    ("schoolmaster", "the classroom", True),
    ("Astronomer", "moon starer", True),
    ("Listen", "silent", True),
    ("funeral", "real fun", True),
]


@pytest.mark.parametrize("s1, s2, expected", test_cases)
def test_isAnagram(s1, s2, expected):
    assert isAnagram(s1, s2) == expected

