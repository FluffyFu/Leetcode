from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if not root:
            return result

        q = Queue()
        q.put(root)

        while not q.empty():
            level_len = q.qsize()
            level_res = []

            for _ in range(level_len):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                level_res.append(node.val)
            result.append(level_res)
        return result

