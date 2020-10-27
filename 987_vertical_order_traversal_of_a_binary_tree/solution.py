from typing import List
from collections import defaultdict
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        positions = defaultdict(list)
        self._dfs(root, x=0, y=0, positions=positions)

        res = []
        for _, vals in sorted(positions.items()):
            res.append([val for _, val in sorted(
                vals, key=lambda x: (-x[0], x[1]))])

        return res

    def _dfs(self, root, x, y, positions):
        if not root:
            return
        positions[x].append((y, root.val))
        self._dfs(root.left, x-1, y-1, positions)
        self._dfs(root.right, x+1, y-1, positions)


class Solution2:
    """
    BFS method
    """

    def vertical_traversal(self, root):
        q = Queue()
        q.put((root, 0, 0))

        positions = defaultdict(list)

        while not q.empty():
            cur, x, y = q.get()
            positions[x].append((y, cur.val))
            if cur.left:
                q.put((cur.left, x-1, y-1))
            if cur.right:
                q.put((cur.right, x+1, y-1))

        res = []
        for _, vals in sorted(positions.items()):
            res.append([val for _, val in sorted(
                vals, key=lambda x: (-x[0], x[1]))])

        return res


"""
        3
       / \
      9  20
         / \
       15   7

dfs(3, 0, 0, {})
    {0: [(0, 3)]}
    dfs(9, -1, -1, pos)
    {0: [(0, 3)], -1: [(-1, 9)]}
    9 done

    dfs(20, 1, -1, pos)
    {0: [(0, 3)], -1: [(-1, 9)], 1: [(-1, 20)]}
        dfs(15, 0, -2, pos)
        {0: [(0, 3), (-2, 15)], -1: [(-1, 9)], 1: [(-1, 20)]}
         15 done
        dfs(7, 2, -2, pos)
        {0: [(0, 3), (-2, 15)], -1: [(-1, 9)], 1: [(-1, 20)], 2: [(-2, 7)]}
        7 done
    20 done
3 done


"""

