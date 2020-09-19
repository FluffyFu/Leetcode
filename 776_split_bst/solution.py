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
        if v > root.val and root.right == None:
            return [root, None]
        if v < root.val and root.left == None:
            return [root, None]
        other_node = self._split_bst(root, v)

        return [root, other_node]

    def _split_bst(self, root: TreeNode, v: int) -> TreeNode:
        """
        Internal helper function to return the node of one of the split tree node.
        """
        if root == None:
            return None
        if v < root.val and root.left == None:
            return root
        if v > root.val and root.right == None:
            return root
        if root.val == v:
            right_node = root.right
            root.right = None
            return right_node
        if v < root.val:
            return self._split_bst(root.left, v)
        if v > root.val:
            return self._split_bst(root.right, v)
