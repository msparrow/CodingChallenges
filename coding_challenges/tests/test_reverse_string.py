import pytest
from solutions.solution_123 import reverse_string  # Replace with your actual solution file path

# Test cases for reverse_string function

def test_empty_string():
    assert reverse_string("") == ""

def test_single_character_string():
    assert reverse_string("a") == "a"

def test_palindrome_string():
    assert reverse_string("madam") == "madam"

def test_lowercase_string():
    assert reverse_string("hello") == "olleh"

def test_uppercase_string():
    assert reverse_string("WORLD") == "DLROW"

def test_mixed_case_string():
    assert reverse_string("Hello World") == "dlroW olleH"

def test_string_with_numbers():
    assert reverse_string("12345") == "54321"

def test_string_with_special_characters():
    assert reverse_string("!@#$%") == "%$#@!"

def test_string_with_spaces():
    assert reverse_string("  hello world  ") == "  dlrow olleh  "

def test_long_string():
    long_string = "This is a very long string to test the reverse string function."
    assert reverse_string(long_string) == ".noitcnuf gnirts esrever eht tset ot gnirts gnol yrev a si sihT"

# Additional test cases for edge cases and boundary conditions:

def test_null_input():
    with pytest.raises(TypeError):
        reverse_string(None)

def test_integer_input():
    with pytest.raises(TypeError):
        reverse_string(123)

def test_list_input():
    with pytest.raises(TypeError):
        reverse_string([1,2,3])


# More test cases for diverse inputs:

test_cases = [
    ("a", "a"),
    ("abc", "cba"),
    ("12345", "54321"),
    ("~!@#$%^&*()_+=-`", "`_-=+)(*&^%$#@!~"),
    ("Hello, World!", "!dlroW ,olleH"),
    ("racecar", "racecar"),
    ("A man, a plan, a canal: Panama", "amanaP :lanac a ,nalp a ,nam A"),
    ("No 'x' in Nixon", "noxiN ni 'x' oN"),
    ("", ""),
    (" ", " "),
    ("1", "1"),
    ("0", "0"),
    ("  ", "  "),
    ("a b c", "c b a"),
    ("   a   ", "   a   "),
    ("你好世界", "界世好你"), # Unicode support
    ("😀😂🤣", "🤣😂😀"), # Emoji support
    ("你好 世界", "界世 好你"), #Unicode with spaces
    ("This is a test", "tset a si sihT"),
    ("Testing123", "321gnitseT"),
    ("leetCode", "edoCteel"),
    ("aBcDeFgHiJkLmNoP", "PoNnMlKjIhGfEdCbA"),
    ("stressed", "desserts"),
    ("Never odd or even", "neve o rrod reveN"),
    ("almostomla", "alomomtsla"),
    ("1234567890", "0987654321"),
    (".,mnbvcxz", "zxcvbnm.,"),
    ("!@#$%^&*()", ")(*&^%$#@!"),
    ("qwertyuiopasdfghjklzxcvbnm", "mnbvcxzlkjhgfdsapoiuytrewq"),
    ("QWERTYUIOPASDFGHJKLZXCVBNM", "MNBVCXZLKJHGFDSAPOIUYTREWQ"),
    ("The quick brown fox jumps over the lazy dog", "god yzal eht revo spmuj xof nworb kciuq ehT"),
    ("apple, banana, cherry", "yrrehc ,ananab ,elppa"),
    ("1000000", "0000001"),
    ("999999", "999999")
]


@pytest.mark.parametrize("input_string, expected_output", test_cases)
def test_reverse_string_parametrized(input_string, expected_output):
    assert reverse_string(input_string) == expected_output