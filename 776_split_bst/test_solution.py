from solution import Solution, TreeNode
import pytest
import pudb


@pytest.fixture
def tree1():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    return root


def test_solution(tree1):
    v = 2
    pudb.set_trace()
    t1, t2 = Solution().splitBST(tree1, v)

    assert t1.val == 4
    assert t2.val == 2
