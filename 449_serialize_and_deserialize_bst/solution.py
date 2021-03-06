class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        res = []
        _serialize(root, res)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        return _deserialize(iter(data.split(',')))


def _serialize(root, res):
    if not root:
        res.append('#')
        return

    res.append(str(root.val))
    _serialize(root.left, res)
    _serialize(root.right, res)


def _deserialize(data):
    cur = next(data)
    if not cur or cur == '#':
        return None
    root = TreeNode(int(cur))
    root.left = _deserialize(data)
    root.right = _deserialize(data)

    return root
