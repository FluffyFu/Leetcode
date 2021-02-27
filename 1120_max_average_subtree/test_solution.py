from solution import max_avg, TreeNode
import pudb


def test():
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(1)

    # pudb.set_trace()

    res = max_avg(root)
    assert res == 6

