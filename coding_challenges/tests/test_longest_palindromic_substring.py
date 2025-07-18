
import pytest
from solutions.solution_101 import longestPalindrome

# Test cases for longestPalindrome function

test_cases = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a"),
    ("bb", "bb"),
    ("abcba", "abcba"),
    ("bananas", "anana"),
    ("racecar", "racecar"),
    ("A man, a plan, a canal: Panama", "a man, a plan, a canal: Panama"), #Handles spaces and punctuation (This might require preprocessing in your solution)
    ("", ""),
    ("aacabdkacaa", "aca"),
    ("abcda", "a"),
    ("abccba", "abccba"),
    ("aaaa", "aaaa"),
    ("bbbbbbbb", "bbbbbbbb"),
    ("abaxyzzyxf", "xyzzyx"),
    ("abcdefghhgfedcba", "abcdefghhgfedcba"),
    ("aabcdcb", "bcacb"),
    ("bananas", "anana"),
    ("million", "illi"),
    ("civil", "ivi"),
    ("level", "level"),
    ("rotor", "rotor"),
    ("stats", "stats"),
    ("detartrated", "detartrated"),
    ("kayak", "kayak"),
    ("repaper", "repaper"),
    ("madam", "madam"),
    ("refer", "refer"),
    ("wow", "wow"),
    ("noon", "noon"),
    ("deified", "deified"),
    ("rotator", "rotator"),
    ("aibohphobia", "aibohphobia"),
    ("noonnoon", "noonnoon"),
    ("racecarracecar", "racecarracecar"),
    ("12321", "12321"),
    ("1221", "1221"),
    ("90009", "90009"),
    ("11211", "11211"),
    ("ababa", "ababa"),
    ("aabbaa", "aabbaa"),
    ("abba", "abba"),
    ("abcddcba", "abcddcba"),
    ("aabcbaaa", "aabcbaa"),
    ("xabcbaxy", "xcbcx"),
    ("xyzzyx", "xyzzyx"),
    ("ccc", "ccc"),
    ("baab", "baab"),
    ("aaba", "aba"),
    ("123454321", "123454321"),
    ("forgeeksskeegfor", "forgeeksskeegfor"),
    ("helloolleh", "helloolleh"),
    ("malayalam", "malayalam")

]


@pytest.mark.parametrize("s, expected", test_cases)
def test_longestPalindrome(s, expected):
    assert longestPalindrome(s) == expected
