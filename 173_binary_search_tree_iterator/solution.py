class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self._res = []
        self._inorder_traverse(root, self._res)
        self._counter = 0
        self._n = len(self._res)

    def _inorder_traverse(self, node, res):
        if not node:
            return
        self._inorder_traverse(node.left, res)
        res.append(node.val)
        self._inorder_traverse(node.right, res)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self._res[self._counter]
        self._counter += 1
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._counter < self._n
