```python
import pytest
from solutions.solution_145 import is_palindrome

# Test cases for Valid Palindrome

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", True),
    (" ", True),
    ("", True),
    ("a", True),
    ("aa", True),
    ("aba", True),
    ("abba", True),
    ("madam", True),
    ("racecar", True),
    ("A man, a plan, a canal: Panama", True),
    (".,", True),
    ("1a2", False),
    ("1a21", True),
    ("0P", False),
    ("OP0", True),
    ("a.", False),
    (".a", False),
    ("a1b1a", True),
    ("a1b2a", False),
    ("00", True),
    ("11", True),
    ("99", True),
    ("race car", True),
    ("Racecar", True),
    ("rAceCar", True),
    ("12321", True),
    ("123321", True),
    ("1234321", True),
    ("!@#$%^&*()_+=-`~[]\{}|;':\",./<>?", True), #all punctuation - edge case for empty string after cleaning
    ("a.", False),
    ("a,", False),
    ("a?", False),
    ("a!", False),
    ("a;", False),
    ("a:", False),
    ("a'", False),
    ("a\"", False),
    ("a#", False),
    ("a$", False),
    ("a%", False),
    ("a^", False),
    ("a&", False),
    ("a*", False),
    ("a(", False),
    ("a)", False),
    ("a_", False),
    ("a=", False),
    ("a-", False),
    ("a+", False),
    ("a`", False),
    ("a~", False),
    ("a[", False),
    ("a]", False),
    ("{a}", False),
    ("}a", False),
    ("|a", False),
    ("a|", False),
    ("a/", False),
    ("a\\", False),
    ("a<", False),
    ("a>", False),
    ("aa..aa", True), # Repeated punctuation


]


@pytest.mark.parametrize("s, expected", test_cases)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected

```