class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_avg(root):
    if not root:
        return 0

    res = [-float('inf')]

    helper(root, res)

    return res[0]


"""
Global counter won't work.
"""


def helper(root, res):
    if not root:
        return 0, 0
    left, cl = helper(root.left, res)
    right, cr = helper(root.right, res)

    cur = root.val + left + right
    res[0] = max(res[0], cur/(cl + cr + 1))

    return cur, cl + cr + 1
