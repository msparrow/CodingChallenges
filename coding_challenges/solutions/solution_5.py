def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)  # Work with positive numbers for easier processing

    reversed_x = 0
    while x > 0:
        pop = x % 10  # Get the last digit
        x //= 10       # Remove the last digit

        # Check for overflow before updating reversed_x
        if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and pop > 7):
            return 0  # Positive overflow
        if reversed_x < -(2**31) // 10 or (reversed_x == -(2**31) // 10 and pop < -8):
            return 0  # Negative overflow

        reversed_x = reversed_x * 10 + pop

    return reversed_x * sign