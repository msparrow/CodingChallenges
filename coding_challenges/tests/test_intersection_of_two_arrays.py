
import pytest
from solutions.solution_131 import intersection

# Test cases for intersection of two arrays

test_cases = [
    ([1, 2, 2, 1], [2, 2], [2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
    ([1, 2], [1, 1], [1]),
    ([1, 2, 3], [4, 5, 6], []),
    ([], [], []),
    ([1], [], []),
    ([], [1], []),
    ([1,1,1,1],[1,1,1,1],[1]),
    ([1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5]),
    ([1,2,3,4,5],[6,7,8,9,10],[]),
    ([1,1,2,2],[2,2,1,1],[1,2]),
    ([1,2,3],[3,2,1],[1,2,3]), #unordered, should maintain order of nums1
    (['a','b','c'],['c','b','a'],['a','b','c']), #test with strings
    ([1,2,3,4,5], [5,4,3,2,1,1,1,1], [1,2,3,4,5]), #duplicates in nums2
    ([1,1,1,1,2,2,2],[1,2],[1,2]), #duplicates in both, no order requirement
    ([1,2,3],[1,2,3,4,5,6],[1,2,3]),
    ([1, 2, 3, 4, 5],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 2, 3, 4, 5]),
    ([10,10,10],[10,10,10],[10]),
    ([-1,-2,-3],[-3,-2,-1],[-1,-2,-3]),
    ([0,0,0],[0,0,0],[0]),
    ([1000000,1000000],[1000000,1000000],[1000000]), #large numbers
    ([1,2,-3,-4,0],[0,-4,-3,2,1],[0,-3,-4,1,2]), #negative numbers and zero
    (['apple','banana','orange'],['orange','apple'],['apple','orange']), #string test case
    ([True,False],[False,True],[False,True]), #boolean test case
    ([1,2,3,4,5],[6,7,8,9,10,1,2,3,4,5],[1,2,3,4,5]), # intersection with duplicates
    ([1,2,3],[1,1,1,2,2,2],[1,2]), #test with lots of duplicates
    ([1,2,2,3,3,3],[2,3,3,4,5,5,5],[2,3]),
    ([1,1,1,2,2,2],[1,1,1,2,2,2,3],[1,2]), #duplicates in both arrays
    ([1,1,1],[1,1,1,2,2,2],[1]), # duplicates in nums2 only
    ([1,2,2,3,3,3],[1,1,1],[1]), #duplicates in nums1 only

    #Edge Cases
    (None, [1,2,3], pytest.raises(TypeError)),
    ([1,2,3], None, pytest.raises(TypeError)),
    (None, None, pytest.raises(TypeError)),
    ([1,2,3], "string", pytest.raises(TypeError)),
    ("string", [1,2,3], pytest.raises(TypeError)),
    ([1,2,[3]],[1,2,3],pytest.raises(TypeError)), #nested list
    ([1,2,3],[1,2,"a"], pytest.raises(TypeError)), #mixed types

    #Large datasets
    (list(range(1000)),list(range(500)),list(range(500))),
    (list(range(1000)),list(range(500,1500)),[]),
    (list(range(1000)),list(range(1000)),list(range(1000))),

    #Repeated elements in both
    ([1,1,1,2,2,3,3,3,4,4],[1,1,2,2,2,3,3,4,4,4],[1,2,3,4]),
    ([1,1,1,1,1],[1,1,1,1,1],[1]),

    #Empty arrays and single element arrays
    ([],[1,2,3],[]),
    ([1,2,3],[],[]),
    ([1],[],[]),
    ([], [1],[ ]),
    ([1],[1],[1]),

    #More edge cases with different datatypes
    ([1,2,3.14],[1,2,3.14],[1,2,3.14]),
    ([1,2,"a"],[1,2,"a"],[1,2,"a"]), #mixed types (this should ideally raise a TypeError but some solutions may handle it)
    ([1, 2, 3], [1, 2, 'a'], pytest.raises(TypeError)), #mixed types should raise TypeError


]


@pytest.mark.parametrize("nums1, nums2, expected", test_cases)
def test_intersection(nums1, nums2, expected):
    if isinstance(expected, Exception):
        with expected:
            intersection(nums1, nums2)
    else:
        assert intersection(nums1, nums2) == expected

