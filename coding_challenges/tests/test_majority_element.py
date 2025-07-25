import pytest
from coding_challenges.solutions.solution_128 import (
    majorityElement_boyermoore as majority_element,
    majorityElement_boyermoore,
    majorityElement_hashmap
)

test_cases = [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([6, 5, 5], 5),
    ([1], 1),
    ([1, 1], 1),
    ([1, 2, 1], 1),
    ([2, 1, 1], 1),
    ([1, 1, 2], 1),
    ([1, 2, 2], 2),
    ([2, 2, 1], 2),
    ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4),
    ([1, 2, 3, 4, 5], -1), # No majority element
    ([1, 2, 3, 4, 5, 5], -1),
    ([], -1), #Empty list
    ([0],0),
    ([0,0,0],0),
    ([0,1,0],0),
    ([1,0,0],0),
    ([0,0,1],0),
    ([1,0,1], 1),
    ([1,1,0],1),
    ([10,20,10,20,10,10,10],10),
    ([10,10,10,20,20,20,20,20],20),
    ([1,1,1,1,2,2,2,2,3],-1),
    ([1,1,1,1,2,2,2,2,3,3,3,3],-1),
    ([-1,1,-1,1,-1,1,1,1,1],1),
    ([-1,-1,1,1,-1,-1,-1,-1,-1],-1),
    ([1, 2, 1, 2, 1, 1, 1],1),
    ([1, 2, 1, 2, 1, 2, 2],2),
    ([100,200,100,100,100,300],100),
    ([100, 200, 300, 400, 100, 100, 100,100], 100),
    ([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3], -1),
    ([1,1,1,2,2,2,3,3,3,4,4,4,4,4,5],-1),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],1),
    ([1]*100 + [2]*99, 1),
    ([1]*99 + [2]*100, 2),
    ([1]*50 + [2]*50, -1),
    ([1]*51 + [2]*49, 1),
    ([1]*49 + [2]*51, 2),
    ('a','a'),
    (['a'], 'a'),
    (['a','b','a'], 'a'),
    (['a','b','c','a','a','a'], 'a'),
    (['a','b','c','d','a','a','a','a'], 'a'),
    (['a','a','b','b','c','c','d','d','e','e','a'], -1),
    ([True,False,True,True],True),
    ([True,False,False,True],-1),
    ([1.0, 1.0, 2.0], 1.0),
    ([1.0, 2.0, 3.0, 4.0, 1.0, 1.0, 1.0], 1.0),
    ([1.5, 1.5, 2.5, 1.5], 1.5),
    ([-1,-1,-1,1,1],-1),
    ([-1,-1,-1,1,1,1],-1),
    ([1,2,3,4,5,6,7,8,9,10],-1)


]

@pytest.mark.parametrize("nums, expected", test_cases)
def test_majority_element(nums, expected):
    assert majority_element(nums) == expected

@pytest.mark.parametrize("nums, expected", test_cases)
def test_majority_element_boyermoore(nums, expected):
    assert majorityElement_boyermoore(nums) == expected

@pytest.mark.parametrize("nums, expected", test_cases)
def test_majority_element_hashmap(nums, expected):
    assert majorityElement_hashmap(nums) == expected