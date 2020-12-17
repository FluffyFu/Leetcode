class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        res = []
        self._serialize(root, res)
        return ','.join(res)

    def _serialize(self, node, res):
        if not node:
            res.append('#')
            return
        res.append(str(node.val))
        self._serialize(node.left, res)
        self._serialize(node.right, res)

    def deserialize(self, data):
        return self._deserialize(iter(data.split(',')))

    def _deserialize(self, data):
        cur = next(data, None)
        if not cur or cur == '#':
            return None
        root = TreeNode(int(cur))
        root.left = self._deserialize(data)
        root.right = self._deserialize(data)
        return root
