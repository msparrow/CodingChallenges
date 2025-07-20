
import pytest
from solutions.solution_98 import sum_numbers, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, TreeNode(2), TreeNode(3)), 25),
    (TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)), 1026),
    (None, 0),
    (TreeNode(0), 0),
    (TreeNode(1), 1),
    (TreeNode(9, TreeNode(8), TreeNode(7)), 195),
    (TreeNode(1, TreeNode(0)), 10),
    (TreeNode(1, None, TreeNode(2)), 12),
    (TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5))), 258),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4, TreeNode(5))), 268),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5)), 1234 + 15),
    (TreeNode(1, TreeNode(2, TreeNode(3)), None), 123),
    (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), 123),
    (TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(8, TreeNode(6), TreeNode(9))), 1116),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), 259),
    (TreeNode(1, TreeNode(1, TreeNode(1)), TreeNode(1, TreeNode(1))), 222),
    (TreeNode(0, TreeNode(0), TreeNode(0)), 0),
    (TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13)))), 831 + 8364 + 8367 + 8101413),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), 12345),
    (TreeNode(9, TreeNode(8, TreeNode(7, TreeNode(6, TreeNode(5))))), 98765)
])
def test_sum_numbers(root, expected):
    assert sum_numbers(root) == expected
