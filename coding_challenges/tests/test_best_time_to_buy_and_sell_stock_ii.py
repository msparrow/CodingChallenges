
import pytest
from solutions.solution_140 import maxProfit

# Test cases for Best Time to Buy and Sell Stock II

test_cases = [
    ([7, 1, 5, 3, 6, 4], 7),  # Example 1
    ([1, 2, 3, 4, 5], 4),  # Increasing sequence
    ([5, 4, 3, 2, 1], 0),  # Decreasing sequence
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), #Long increasing sequence
    ([10,9,8,7,6,5,4,3,2,1],0), #Long decreasing sequence
    ([7,6,4,3,1],0), #Long decreasing sequence
    ([1,7,1,7,1,7], 12), # alternating peaks and troughs
    ([3,2,6,5,0,3], 7), #various peaks and valleys
    ([1], 0),  # Single element
    ([], 0),  # Empty array
    ([1,1,1,1,1],0), #all same element
    ([2,1,2,0,1], 2), #several peaks and troughs
    ([2,4,1], 1), # simple case
    ([1,2,4,2,5,7,2,4,9,0], 16), # complex case with many peaks and troughs
    ([0,2,0,2,0,2,0,2,0], 8), # alternating 0 and 2
    ([1, 0, 1, 0, 1, 0, 1,0,1,0],8), # alternating 0 and 1
    ([10,9,8,7,6,5,4,3,2,1,10], 1), #Single upward spike
    ([1,10,2,9,3,8,4,7,5,6],15), # many peaks and troughs
    ([5,4,3,2,1,6],5), # single spike at the end
    ([6,1,2,3,4,5], 9), # single spike at beginning
    ([1,2,3,4,5,6,0], 15), # spike at end
    ([0,1,2,3,4,5,6],6), # increasing
    ([6,5,4,3,2,1,0],0), # decreasing
    ([7, 1, 5, 3, 6, 4, 10, 11, 8], 17), #More complex with higher values
    ([1, 2, 4, 2, 5, 7, 2, 4, 9, 15, 1, 11], 29), # many fluctuations
    ([10, 20, 30, 40, 50], 40), # simple increasing sequence
    ([50, 40, 30, 20, 10], 0), #simple decreasing sequence
    ([10, 11, 7, 10, 12, 6], 10), # various fluctuations
    ([1, 3, 2, 8, 4, 9], 15), #various fluctuations
    ([4, 1, 2, 1, 1, 2], 2), # small fluctuations
    ([1,2,1,2,1,2,1,2,1,2],4), #small alternating pattern
    ([2,1,2,1,2,1,2,1,2,1],4), #small alternating pattern
    ([100,180,260,310,40,535,695], 1075), #large values
    ([0,0,0,0,0],0), #all zeros
    ([10, 10, 10, 10, 10], 0), #all same
    ([1, 5, 2, 7, 3, 9, 4, 11, 5, 13], 31), #long sequence
    ([13, 11, 9, 7, 5, 3, 1, 1, 1, 1], 0), #decreasing then all same
    ([1,1,1,1,2,2,2,2,3,3,3,3], 4), # steps
    ([3,3,3,3,2,2,2,2,1,1,1,1],0), #descending steps
    ([-1,-2,-3,-4,-5],0), #negative numbers
    ([-1,0,1,0,-1], 2), #negative and positive numbers
    ([-5,-4,-3,-2,-1,0],0), #negative increasing sequence
    ([0, -1, -2, -3, -4, -5], 0), #decreasing negative numbers
    ([-5, -2, -1, 0, 2, 3, 1, -1], 7), # mixed negative and positive
    ([10, 5, 15, 10, 20], 25),  # more complex cases
    ([1, 2, 0, 3, 0, 1], 4),  # zeroes interspersed
    ([0, 1, 0, 1, 0, 1], 2),  # alternating 0 and 1
    ([2, 1, 4, 5, 2, 9, 7], 11), #various peaks and valleys
    ([1,10,1,10,1,10],24), #alternating 1 and 10
    ([10,1,10,1,10,1], 24) #alternating 1 and 10


]

@pytest.mark.parametrize("prices, expected", test_cases)
def test_maxProfit(prices, expected):
    assert maxProfit(prices) == expected
