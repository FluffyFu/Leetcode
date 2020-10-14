from solution import TreeNode, Solution
import pytest
import pudb


@pytest.fixture
def tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(4)
    root.right.right = TreeNode(4)

    return root


def test_solution(tree):
    res = Solution().find_duplicate_subtrees(tree)
    assert len(res) == 2
