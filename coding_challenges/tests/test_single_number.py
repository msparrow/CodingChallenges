```python
import pytest
from solutions.solution_134 import singleNumber  # Assuming your solution is in this file

# Test cases for singleNumber function

test_cases = [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1),
    ([0],0),
    ([1,1,2,2,3,3,4,4,5], 5),
    ([1,0,1], 0),
    ([99], 99),
    ([-1,-1,2], 2),
    ([2,-1,-1], 2),
    ([0,1,0,1,2], 2),
    ([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10], 10),
    ([], 0), #Edge case: empty list
    ([1,1,1,1,1,2], 2),
    ([2,1,1,1,1,1], 2),
    ([1,1,1,1,1,1,2,2,2,2,2,3],3),
    ([2,1,1,1,1,1,2,2,2,2,2,2], 3), #Edge case: Multiple duplicates
    ([-1,2,-1],2),
    ([0,0,0,0,0,0,1], 1),
    ([1,0,0,0,0,0,0], 1),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2], 2), #Edge case: many duplicates
    ([1000,2,1000],2),
    ([1000,1000,3000,3000,4], 4),
    ([-1000,2,-1000],2),
    ([float('nan'),1,float('nan')],1), #Edge case: NaN
    ([float('inf'),1,float('inf')],1), #Edge case: infinity
    ([-float('inf'),1,-float('inf')],1), #Edge case: negative infinity
    ([float('inf'),float('inf'),1, float('-inf'),float('-inf')], 1), #Edge case: mix of inf and -inf


    #Large test cases:
    (list(range(1000)) + list(range(1000)) + [1001], 1001),
    (list(range(10000)) + list(range(10000)) + [10001], 10001),
    (list(range(100000)) + list(range(100000)) + [100001], 100001),
    ([1]*1000 + [2], 2),
    ([2]*1000 + [1], 1),
    ([1]*10000 + [2], 2),
    ([2]*10000 + [1], 1),
    ([1]*100000 + [2], 2),
    ([2]*100000 + [1], 1),

    #Test cases with repeated numbers:
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],2),
    ([1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3],3),
    ([1]*10 + [2]*10 + [3]*10 + [4],4),

    # Edge cases with negative numbers and zeros:
    ([-1, -2, 0, -1, -2], 0),
    ([-10, -10, 5, 0, 0, 5],0),
    ([0,0,0,0,0,1,1,1,1],1),
    ([0,0,0,0,0,-1,-1,-1],-1),

    #More diverse test cases:
    ([5,4,3,2,1,5,4,3,2,1,0],0),
    ([0,1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1,0], 1),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],2),
    ([5, 5, 2, 2, 1, 1, 100, 100, 3, 3], 1)

]


@pytest.mark.parametrize("nums, expected", test_cases)
def test_singleNumber(nums, expected):
    assert singleNumber(nums) == expected
