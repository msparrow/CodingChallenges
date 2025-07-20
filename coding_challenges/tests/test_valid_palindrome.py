import pytest
from solutions.solution_145 import is_palindrome

# Test cases for Valid Palindrome
# Description: Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring case.

test_cases = [
    # --- Basic Cases ---
    ("A man, a plan, a canal: Panama", True),  # Classic example
    ("racecar", True),  # Simple palindrome
    ("hello", False),  # Simple non-palindrome
    
    # --- Edge Cases ---
    ("", True),  # Empty string
    (" ", True),  # String with only a space (becomes empty)
    ("a", True),  # Single character
    (".,", True),  # String with only punctuation (becomes empty)

    # --- Case Insensitivity ---
    ("Level", True),
    ("Noon", True),
    ("aA", True),
    ("abA", True),

    # --- Alphanumeric Filtering ---
    ("race a car", False),  # "raceacar" is not a palindrome
    ("Was it a car or a cat I saw?", True),
    ("Don't nod.", True),
    ("Eva, can I see bees in a cave?", True),
    ("Red rum, sir, is murder.", True),
    ("No 'x' in Nixon", True),

    # --- Numeric Palindromes ---
    ("12321", True),
    ("1a1", True),
    ("12345", False),
    ("a1b2a", False),
    ("0P", False),
]

@pytest.mark.parametrize("s, expected", test_cases)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
