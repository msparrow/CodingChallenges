
import pytest
from solutions.solution_137 import TreeNode, invertTree

# Test cases for Invert Binary Tree

# Helper function to create a tree from a list
def create_tree(data):
    if not data:
        return None
    root = TreeNode(data[0])
    queue = [root]
    i = 1
    while queue and i < len(data):
        node = queue.pop(0)
        if data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1
    return root


# Helper function to convert tree to list for comparison
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    #remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


@pytest.mark.parametrize("input_data, expected_output", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([1], [1]),
    ([], []),
    ([1, None, 2], [1,2, None]),
    ([1,2, None, None, None, 3], [1, None, 2, None, 3, None]),
    ([4,2,7,1,3,6,9,None,None,None,None,None,None,None,None], [4,7,2,9,6,3,1,None,None,None,None,None,None,None,None]),
    ([4,2,7,1,3,6,9,10,11,12,13,14,15,16,17],[4,7,2,9,6,3,1,17,16,15,14,13,12,11,10]),
    ([1,2,3,4,5,6,7], [1,3,2,7,6,5,4]),
    ([1,None,2,3], [1,2,None,None,None,3]),
    ([1,None,2,None,None,3,None,4,5], [1,2,None,None,None,3,None,5,4]),
    ([0,2,4,1,None,3,None,None,5,None,6],[0,4,2,None,6,3,None,5,None,None,None,None,None,None,None]),
    ([1,2,2,3,4,4,3], [1,2,2,3,4,4,3]),
    ([0], [0]),
    ([0,1],[0,1]),
    ([0,None,1],[0,1,None]),
    ([0,1,None,None,2],[0,1,None,None,2]),
    ([1,None,2],[1,2,None]),
    ([1,2,None],[1,None,2]),
    ([1,None,None,2,3],[1,None,None,3,2]),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[1,3,2,7,6,5,4,15,14,13,12,11,10,9,8]),
    ([5,1,9,3,7,None,15,None,None,11,None,13,None,14], [5,9,1,15,None,7,3,None,None,13,None,11,None,14]),
    # Add more test cases as needed, covering various scenarios like:
    # - Empty tree
    # - Tree with only one node
    # - Perfectly balanced tree
    # - Unbalanced tree
    # - Tree with only left or right subtrees
    # - Tree with None values for some nodes

    # Test Cases with more than 15 nodes.
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[1,3,2,7,6,5,4,15,14,13,12,11,10,9,8,16]),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[1,3,2,7,6,5,4,15,14,13,12,11,10,9,8,17,16]),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],[1,3,2,7,6,5,4,15,14,13,12,11,10,9,8,17,16,18]),
])
def test_invert_tree(input_data, expected_output):
    root = create_tree(input_data)
    inverted_root = invertTree(root)
    assert tree_to_list(inverted_root) == expected_output
