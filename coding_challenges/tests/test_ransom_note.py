
import pytest
from solutions.solution_132 import can_construct_ransom_note as canConstruct

# Test cases for canConstruct function

test_cases = [
    # Positive cases
    ("aa", "aab", True),
    ("a", "b", False),
    ("aa", "aa", True),
    ("abc", "abc", True),
    ("aaabbcc", "aabbcca", True),
    ("aaabbcc", "aabbccaa", True), # extra 'a' should be okay
    ("a", "aa", True),
    ("", "", True), # Empty strings
    ("hello", "hello world", True),
    ("world", "hello world", True),
    ("helloworld", "helloworld", True),
    ("this is a test", "this is a test string", True),
    ("onetwothree", "onetwothreefourfive", True),


    # Negative cases
    ("aa", "a", False),
    ("abc", "ab", False),
    ("aab", "aa", False),
    ("aabbcc", "aa bb cc", False), #space separated, should be false.
    ("abc", "bca", False), #Different order should be false.
    ("aa", "aba", False),
    ("hello world", "hello", False),
    ("onetwothreefourfive", "onetwothree", False),
    ("this is a longer string", "this is a shorter string", False),
    ("this is a test", "this is a different test", False),
    ("", "a", False), #Empty ransom note, non-empty magazine
    ("a", "", False), #Non-empty ransom note, empty magazine


    # Edge cases
    ("a"*1000, "a"*1000, True), #Large string
    ("a"*1001, "a"*1000, False), #Slightly larger ransom note
    ("a"*1000, "a"*1001, True), #Slightly larger magazine
    (" ", " ", True), #Single space
    ("  ", "  ", True), #Double space
    ("a b", "a b", True), #Space in ransom note and magazine
    ("a b", "a  b", True), #Extra space in magazine
    ("a b", "ab", True), #No space in magazine
    ("ab", "a b", True), #No space in ransom note

    #More complex scenarios
    ("This is a test.", "This is a test. This is a longer string.", True),
    ("Testing 123!", "Testing 123! This is a longer string.", True),
    ("Longer string test.", "This is a test. This is a longer string.", False),
    ("Another test string", "A completely different string", False),
    ("One more complex test case.", "This is another really complex test case.", False),
    ("Short", "Short and Sweet", True),
    ("Short and Sweet", "Short", False),
    (" ", "a", False), #space vs char
    ("a", " ", False), #char vs space
    ("123", "1234567890", True), # Numbers
    ("1234567890", "123", False), # Numbers, reversed
    ("~!@#$%^&*()_+=-`", "~!@#$%^&*()_+=-`", True), #Special Characters
    ("~!@#$%^&*()_+=-`", "!@#$%^&*()_+=-`", False), #Missing special char
    ("The quick brown fox jumps over the lazy fox.", "The quick brown fox jumps over the lazy dog.", False), #Similar strings with one word diff.
    (" ", "", False), #Space in ransom note, empty magazine
    ("", " ", False), #Empty ransom note, space in magazine


    # Cases with repeated characters
    ("aabbbccc", "aaabbbccc", True),
    ("aabbbccc", "aaabbbcccd", True),
    ("aabbbccc", "aaabbcc", False),
    ("bbbaaa", "aaabbb", True),
    ("bbbaaa", "aabbb", False),


]

@pytest.mark.parametrize("ransomNote, magazine, expected", test_cases)
def test_canConstruct(ransomNote, magazine, expected):
    assert canConstruct(ransomNote, magazine) == expected

