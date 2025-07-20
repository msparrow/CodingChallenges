import pytest
from solutions.solution_126 import isSubtree

# Test cases for isSubtree function

test_cases = [
    # Basic Cases
    ((1, 2, 3), (3,), True),
    ((1, 2, 3), (4,), False),
    ((1, 2, 3), (1, 2), True),
    ((1, 2, 3), (1, 2, 3), True),
    ((1, 2, 3), (2, 3), True),
    ((1, 2, 3), (1, 2, 4), False),
    ((1, None, 2), (2,), True),
    ((1, 2, None), (2,), True),
    ((1, None, None), (1,), True),
    ((1, None, None), (2,), False),

    # More Complex Cases
    ((3, 4, 5, 1, 2), (4, 1, 2), True),
    ((3, 4, 5, 1, 2), (4, 1, 3), False),
    ((3, 4, 5, 1, 2, None, 6, 7, 8), (1, 2, None, 6, 7, 8), True),
    ((3, 4, 5, 1, 2, None, 6, 7, 8), (1, 2), True),
    ((3, 4, 5, 1, 2, None, 6, 7, 8), (1, 2, 6), False),  #Checking for correct subtree structure

    # Cases with None values
    ((1, None, 2, None, None, None, 3), (2, None, 3), True),
    ((1, None, 2, None, None, None, 3), (2, None, 4), False),
    ((1, None, 2), (None,), False), #Subtree is just None
    ((None,), (None,), True), #Both are None
    ((1, None, 2), (1,), True),
    ((1, 2, 3, 4, 5), (4, 5), True),
    ((1, 2, 3, 4, 5), (4, 6), False),


    # Larger Trees
    ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (4, 5, 6, 7), True),
    ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (11,), False),
    ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3), True),
    ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1,2,3,4,5,6,7,8,9,11), False),

    #Edge Cases - identical trees
    ((1,2,3),(1,2,3),True),
    ((1),(1),True),
    ((None),(None),True),


    #Repeated nodes
    ((1,2,1,3,4),(1,3,4),True),
    ((1,2,1,3,4),(1,2,1),True),
    ((1,2,1,3,4),(2,1,4),False),


    #Unbalanced trees
    ((1,2,3,4,5,6,7),(7,),True),
    ((1,2,3,4,5,6,7),(1,2,3,4,5,6,7),True),
    ((1,2,3,4,5,6,7),(1,2,3,4,5,6,8),False),


    #More complex unbalanced trees

    ((1,2,None,4,5,None,7),(4,5,None,7),True),
    ((1,2,None,4,5,None,7),(1,2,None,4,5,None,8),False),
    ((1,2,3,4,None,6,7,None,8,9,10),(4,None,6,7,None,8,9,10),True),
    ((1,2,3,4,None,6,7,None,8,9,10),(4,None,6,7,None,8,9,11),False),


    # Test cases with lists instead of tuples
    ([1, 2, 3], [3], True),
    ([1, 2, 3], [1, 2], True),
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2, 3], [2, 3], True),
    ([1, 2, 3], [4], False),
    ([1, None, 2], [2], True),
    ([1, None, None], [2], False),


    # Empty Tree Cases
    ([], [], True),
    ([1,2,3], [], False),
    ([], [1], False),


    #Edge case with empty subtrees within larger tree
    ([1,2,None,4],[1,2,None,4],True),
    ([1,2,None,4],[4],True),
    ([1,2,3,None,5],[2,3,None,5],True)


]

@pytest.mark.parametrize("root1, root2, expected", test_cases)
def test_isSubtree(root1, root2, expected):
    assert isSubtree(root1, root2) == expected
