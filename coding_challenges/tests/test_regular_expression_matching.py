
import pytest
from solutions.solution_104 import isMatch

# Test cases for regular expression matching

test_cases = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
    ("aa", "aa", True),
    ("aaa", "a*", True),
    ("aaa", "aa", False),
    ("ab", ".*c", False),
    ("aab", "a*b", True),
    ("a", "ab*", True),
    ("a", ".*..a*", False),
    ("a", "a.", False),
    ("ab", ".*", True),
    ("abc", ".*", True),
    ("abcd", ".*", True),
    ("mississippi", "mis*is*ip*.", True),
    ("mississippi", "mis*is*p*.", False),
    ("", ".*", True),
    ("", "", True),
    ("a", ".*", True),
    ("a", "a*", True),
    ("a", ".*a*", True),
    ("a", "a?", True),
    ("a", "ab*", True),
    ("a", ".*b*", True),
    ("aa", "a*", True),
    ("aa", "aa", True),
    ("aa", "a*a", True),
    ("aa", ".*a*", True),
    ("aa", "a?a?", True),
    ("aab", "c*a*b", True),
    ("aab", "a*a*", True),
    ("aab", "a*b*", True),
    ("aab", "a*.*", True),
    ("aab", "a*b", True),
    ("aaa", "a*", True),
    ("aaa", "aa", False),
    ("aaa", "a*a*", True),
    ("aaa", "a*a?a?", True),
    ("ab", ".*c", False),
    ("abc", "ab*c", True),
    ("abbc", "ab*c", True),
    ("abbc", "ab*c*", True),
    ("abbc", "a*b*c*", True),
    ("abc", "abc", True),
    ("abc", "a.c", True),
    ("abc", "a.*c", True),
    ("abc", "ab*", True),
    ("ab", ".*c", False),
    ("a", ".*b*", True),
    ("a", "b*", False),
    ("ab", "a*b*", True),
    ("a", "ab*", True),
    ("a", "a*", True)


]


@pytest.mark.parametrize("s, p, expected", test_cases)
def test_isMatch(s, p, expected):
    assert isMatch(s, p) == expected

```