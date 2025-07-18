
import pytest
from solutions.solution_136 import TreeNode, diameterOfBinaryTree

# Test cases for diameterOfBinaryTree

test_cases = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5, None, None, None, 6], 4),
    ([1, 2, 3, 4, 5, None, None, None, 6, 7, 8], 5),
    ([1], 0),
    ([1, 2], 1),
    ([1, None, 2], 1),
    ([1, 2, None, 3], 2),
    ([1, None, 2, None, 3, None, 4], 3),
    ([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,8,None,-1,None,None,-8,None,None,None,None,None,None,None,7,4,None,-2,None,-5], 7),
    ([], 0),  # Empty tree
    ([3,9,20,None,None,15,7], 3),
    ([1,2,3,4,5,6,7],5),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 13), #Fullish Tree
    ([1,2],1),
    ([1, None, 2], 1),
    ([1,2,None,3,4,None,None,5,None,None,6],5), #Slightly unbalanced
    ([1, None, 2, None, None, 3, 4], 3), #Unbalanced 
    ([1,2,2,3,3,None,None,4,4], 4), #Very unbalanced
    ([1,2,2,3,3,3,3,4,4,4,4,4,4,4,4],7), #Extra unbalanced

    # More complex test cases with various tree structures
    ([5,4,3,1,1,None,7,0,0,None,6,8,None,None,None,None,None,None,None,None,None,None,None,None,None,None], 7),
    ([1,2,2,3,4,4,3], 4),
    ([1,5,2,None,None,3,4,None,None,None,None,None,None,6], 4),
    ([1,None,2,3,None,4,None,None,5],4),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 18),
    ([10,5,-3,3,2,None,11,3,-2,None,1],7),
    ([1,2,3,4,5,6,7,8,9,10],8),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],14),
    ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 8),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 14),
    ([1, None, 2, None, None, 3, 4, None, None, None, None, None, None, 5], 4),

    #Edge Cases
    (None,0), #Empty Tree
    ([1, None],0), #Single Node with empty right child
    ([1,2,None],1), #Single Node with empty left and right child

    # Repeated Values
    ([1,1,1,1,1,1,1],6),
    ([1,1,1,None,None,1,1],4),
    ([1,None,1,1,None,1,None,None,None,1],4),

    #Negative Values
    ([-1,-2,-3,-4,-5],4),
    ([-1,None,-2,None,None,-3,-4],3),


    # Test cases with large trees
    ([i for i in range(100)], 98),  # Large balanced tree (approximation)
    ([i for i in range(1,101)],98), #Large Tree



    # Add more test cases here as needed...

]


@pytest.mark.parametrize("tree_input, expected", test_cases)
def test_diameter_of_binary_tree(tree_input, expected):
    # Convert list representation to TreeNode
    if tree_input:
        root = TreeNode(tree_input[0])
        nodes = [root]
        i = 1
        while nodes:
            curr = nodes.pop(0)
            if i < len(tree_input) and tree_input[i] is not None:
                curr.left = TreeNode(tree_input[i])
                nodes.append(curr.left)
            i += 1
            if i < len(tree_input) and tree_input[i] is not None:
                curr.right = TreeNode(tree_input[i])
                nodes.append(curr.right)
            i += 1
        
        result = diameterOfBinaryTree(root)
        assert result == expected
    else:
        assert diameterOfBinaryTree(None) == 0
