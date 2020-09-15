from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self._max_depth(root)

    def _max_depth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self._max_depth(root.left), self._max_depth(root.right)) + 1


class SolutionBFS:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        q = Queue()
        q.put(root)

        tree_depth = 0
        while not q.empty():
            tree_depth += 1
            level_len = q.qsize()

            for _ in range(level_len):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
        return tree_depth
