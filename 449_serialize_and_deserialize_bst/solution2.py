from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Using the BST property, we can the value range to determine if the current
node is done. Comparing with serialize and deserialize a BT, we don't need to
add indicator for empty nodes.
"""


class Codec:

    def serialize(self, root: TreeNode) -> str:
        res = []
        _serialize(root, res)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        return _deserialize(deque(data.split(',')), -float('inf'), float('inf'))


def _deserialize(q, low, high):
    if not q:
        return None
    val = int(q[0])

    if (val < low or val > high):
        return
    q.popleft()
    root = TreeNode(val)
    root.left = _deserialize(q, low, val-1)
    root.right = _deserialize(q, val+1, high)

    return root


def _serialize(root, res):
    if not root:
        return
    res.append(str(root.val))
    _serialize(root.left, res)
    _serialize(root.right, res)

