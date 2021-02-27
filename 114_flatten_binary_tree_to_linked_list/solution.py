class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
    if not root:
        return root

    res = []
    pre_order(root, res)

    for i in range(len(res)-1):
        res[i].left = None
        res[i].right = res[i+1]

    res[-1].left = None
    res[-1].right = None


def pre_order(root, res):
    if not root:
        return
    res.append(root)
    pre_order(root.left, res)
    pre_order(root.right, res)

