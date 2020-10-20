from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = Queue()
        q.put(root)
        res = []

        while not q.empty():
            level_n = q.qsize()
            cur = None
            for _ in range(level_n):
                cur = q.get()
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            res.append(cur.val)

        return res


class Solution2:
    def right_side_view(self, root):
        if not root:
            return []

        level = [root]
        res = []
        while level:
            res.append(level[-1].val)
            level = [k for node in level for k in (node.left, node.right) if k]

        return res


"""
        1
      /    \
    2       3
      \      \
       5      4

q = [1], level_n = 1, cur = 1, res = [1]
q = [2, 3], level_n = 2, q = [3, 5], cur = 3, q = [5, 4], res = [1, 3]
q= [5, 4], level_n = 2, cur = 5, cur = 4, res = [1, 3, 4]

"""

