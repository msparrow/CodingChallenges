
import pytest
from solutions.solution_124 import firstUniqChar

# Test cases for firstUniqChar function

test_cases = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabbcc", -1),
    ("", -1),
    ("a", 0),
    ("aa", -1),
    ("aba", 0),
    ("babc", 1),
    ("aabbccddeeffgghhiiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz", -1),
    ("zabcdefghijklmnopqrstuvwxyz", 0),
    ("abcdefghijklmnopqrstuvwxyz", 0),
    ("thedailybyte", 2),
    ("programming", 0),
    ("algorithms", 0),
    ("datastructures", 0),
    ("interview", 0),
    ("preparation", 0),
    ("practice", 0),
    ("coding", 0),
    ("challenges", 0),
    ("python", 0),
    ("javascript", 0),
    ("java", 0),
    ("cpp", 0),
    ("c#", 0),
    ("swift", 0),
    ("kotlin", 0),
    ("go", 0),
    ("ruby", 0),
    ("php", 0),
    ("perl", 0),
    ("r", 0),
    ("sql", 0),
    ("nosql", 0),
    ("cloud", 0),
    ("devops", 0),
    ("testing", 0),
    ("debugging", 0),
    ("design", 0),
    ("architecture", 0),
    ("security", 0),
    ("performance", 0),
    ("scalability", 0),
    ("availability", 0),
    ("maintainability", 0),
    ("refactoring", 0),
    ("unittesting", 0),
    ("integrationtesting", 0),
    ("systemtesting", 0),
    ("usertesting", 0),
    ("acceptance testing", 0),
    ("stress testing", 0),
    ("load testing", 0)

]


@pytest.mark.parametrize("s, expected", test_cases)
def test_firstUniqChar(s, expected):
    assert firstUniqChar(s) == expected
