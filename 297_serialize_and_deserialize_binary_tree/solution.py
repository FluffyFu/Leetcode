# Definition for a binary tree node.
from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecPreOrder:

    def serialize(self, root):
        """
        Use pre-order traversal to serialize the tree
        """
        res = []
        self._serialize(root, res)
        res = ','.join(str(e) for e in res)
        return res

    def _serialize(self, root, res):
        if not root:
            res.append('#')
            return
        res.append(root.val)
        self._serialize(root.left, res)
        self._serialize(root.right, res)

    def deserialize(self, data):
        """
        """
        if not data:
            return None
        root = self._deserialize(iter(data.split(',')))

        return root

    def _deserialize(self, data):
        cur = next(data, None)
        if not cur:
            return None
        if cur == '#':
            return None
        parent = TreeNode(int(cur))
        parent.left = self._deserialize(data)
        parent.right = self._deserialize(data)
        return parent


class CodecPostOrder:

    def serialize(self, root):
        res = []
        self._serialize(root, res)
        return ','.join(res)

    def _serialize(self, root, res):
        if not root:
            res.append('#')
            return
        self._serialize(root.left, res)
        self._serialize(root.right, res)
        res.append(str(root.val))

    def deserialize(self, data):
        if not data:
            return None
        data = data.split(',')
        root = self._deserialize(data)
        return root

    def _deserialize(self,  data):
        if not data:
            return None
        cur = data.pop()
        if cur == '#':
            return None
        root = TreeNode(int(cur))
        root.right = self._deserialize(data)
        root.left = self._deserialize(data)

        return root


class CodecLevelOrder:
    """
    Serialize the binary tree level-by-level.
    """

    def serialize(self, root):
        if not root:
            return ''
        res = []
        q = Queue()
        q.put(root)

        while not q.empty():
            cur = q.get()
            if cur:
                res.append(str(cur.val))
                q.put(cur.left)
                q.put(cur.right)
            else:
                res.append('#')

        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q = Queue()
        q.put(root)

        i = 1
        while not q.empty():  # or using i < len(data), they are compatible
            parent = q.get()
            if data[i] != '#':
                parent.left = TreeNode(int(data[i]))
                q.put(parent.left)
            i += 1

            if data[i] != '#':
                parent.right = TreeNode(int(data[i]))
                q.put(parent.right)
            i += 1

        return root


"""
i = 1, parent = 1, data[1] = 2, q = [2]
i = 2, data[2] = 3, q = [2, 3]
i = 3, parent = 2, data[3] = '#', q = [3]
i = 4, parent = 2, data[4] = '#', q = [3]
i = 5, parent = 3, data[5] = 4, q = [4]
i = 6, parent = 3, data[6] = 5, q = [4, 5]
"""

