from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: TreeNode, v: int) -> List[TreeNode]:
        if root == None:
            return [None, None]
        if v < root.val:
            left, right = self.splitBST(root.left, v)
            root.left = right
            return [left, root]
        elif v > root.val:
            left, right = self.splitBST(root.right, v)
            root.right = left
            return [root, right]
        elif v == root.val:
            right = root.right
            root.right = None
            return [root, right]
