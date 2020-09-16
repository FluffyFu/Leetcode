from typing import List
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if not root:
            return result
        q = Queue()
        q.put(root)
        left_to_right = True

        while not q.empty():
            level_len = q.qsize()
            sub_result = []

            for _ in range(level_len):
                node = q.get()
                sub_result.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            if left_to_right:
                result.append(sub_result)
            else:
                result.append(sub_result[::-1])
            left_to_right = (not left_to_right)
        return result

