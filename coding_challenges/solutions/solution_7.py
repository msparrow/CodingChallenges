
def is_palindrome(x):
    if x < 0:
        return False

    # Handle single-digit numbers (they are palindromes)
    if x < 10:
        return True

    original_number = x
    reversed_number = 0

    # Reverse the number using integer arithmetic
    while x > 0:
        digit = x % 10  # Extract the last digit
        reversed_number = reversed_number * 10 + digit  # Add the digit to the reversed number
        x //= 10  # Remove the last digit from x

    # Compare the original and reversed numbers
    return original_number == reversed_number
