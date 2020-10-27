from typing import List
from collections import defaultdict
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        q = Queue()
        q.put(root)

        while not q.empty():
            cur = q.get()
            if cur.left:
                q.put(cur.left)
                graph[cur].append(cur.left)
                graph[cur.left].append(cur)
            if cur.right:
                q.put(cur.right)
                graph[cur].append(cur.right)
                graph[cur.right].append(cur)

        q = Queue()
        visited = set()
        q.put(target)
        visited.add(target)

        while not q.empty() and k > 0:
            level_l = q.qsize()
            for _ in range(level_l):
                cur = q.get()
                for v in graph[cur]:
                    if v not in visited:
                        visited.add(v)
                        q.put(v)
            k -= 1
        res = []
        while not q.empty():
            res.append(q.get().val)
        return res


"""
         3
        / \
       5   1
      / \  | \
    6   2  0   8
       / \
      7   4
"""

