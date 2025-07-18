```python
import pytest
from solutions.solution_121 import max_profit

# Test cases for Best Time to Buy and Sell Stock

test_cases = [
    ([7, 1, 5, 3, 6, 4], 5),  # Basic case
    ([7, 6, 4, 3, 1], 0),  # Decreasing prices
    ([1, 2, 3, 4, 5], 4),  # Increasing prices
    ([5, 4, 3, 2, 1], 0),  # Decreasing prices
    ([1], 0),  # Single element
    ([], 0),  # Empty array
    ([2, 4, 1], 2), # Case with a dip
    ([1,2,1,2,0,3], 3), #More complex case
    ([3,2,6,5,0,3], 4), #More complex case
    ([1,3,2,8,4,9], 8), #More complex case
    ([9,8,7,6,5,4,3,2,1], 0), # Decreasing
    ([1,2,3,4,5,6,7,8,9], 8), # Increasing
    ([2,1,2,0,1], 1), #Another complex case
    ([0,1,2,0,1,2], 2), #Another complex case
    ([2,0,1,1,1], 1), #Another complex case
    ([1,1,1,1,1], 0), #All same
    ([0,0,0,0,0],0), #All zeros
    ([100,101,102,103,104], 4), # Larger numbers
    ([104,103,102,101,100], 0), #Larger numbers decreasing
    ([1, 5, 2, 8, 1, 9, 3], 8),  # Multiple peaks and valleys
    ([9, 1, 5, 3, 6, 4, 7, 2], 6), #Another multi peak and valley case
    ([1,2,4,2,5,7,2,4,9,0], 8), #Another complex case
    ([0,6,0,7,0,5,0,8], 8), #Multiple zeros
    ([7, 0, 6, 1, 5, 2, 8, 3], 7), #More complex
    ([3,2,1,0,-1,-2], 0), #Negative numbers
    ([-1,-2,-3,-4,-5], 0), #Negative decreasing
    ([-5,-4,-3,-2,-1], 0), #Negative Increasing
    ([-2, -1, 0, 1, 2], 2), #Negative to positive
    ([2, 1, -1, -2, -3], 1), #Positive to negative
    ([1000, 1001, 1002, 999], 1), #test around 1000
    ([999, 1000, 1001, 1002], 3), #test around 1000
    ([5,5,5,5,5,5],0), #all same number test
    ([1000000, 1000001, 1000002, 1000003], 3), #Large numbers test
    ([1000003, 1000002, 1000001, 1000000], 0), #Large numbers decreasing test
    ([0,1,0,1,0,1],1), # alternating 0,1
    ([1,0,1,0,1,0], 1), #alternating 1,0
    ([2,1,1,1,1,1],1), #leading high
    ([1,1,1,1,1,2], 1), #trailing high
    ([1, 2, 3, 4, 0], 4), #ending with 0
    ([0, 1, 2, 3, 4], 4), #starting with 0
    ([4, 3, 2, 1, 0], 0), #decreasing from 4
    ([10, 9, 8, 7, 6], 0), #decreasing from 10
    ([6, 7, 8, 9, 10], 4), #increasing from 6
    ([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 9), #random order
    ([6, 5, 4, 3, 2, 1, 0], 0), # Decreasing from 6
    ([0, 1, 2, 3, 4, 5],5), # Increasing from 0
    ([5, 0, 4, 1, 3, 2], 4), # Random numbers with 0
    ([0, 2, 0, 3, 0, 4], 4), # Random numbers with multiple 0s
    ([4, 3, 0, 1, 2], 2), #decreasing then increasing with 0
    ([2,1,0,1,2],2), # V shaped curve
    ([2, 5, 1, 6, 3, 7], 5), # complex case with different peaks
    ([7, 3, 1, 2, 5, 4, 6], 5), #another complex case
    ([1, 5, 2, 4, 3, 6], 5), # another complex case

]


@pytest.mark.parametrize("prices, expected", test_cases)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected

```