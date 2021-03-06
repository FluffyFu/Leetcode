class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if root == None:
            return False
        if (root.left == None) and (root.right == None) and (target == root.val):
            return True

        return self.hasPathSum(root.right, target-root.val) or self.hasPathSum(
            root.left, target-root.val
        )

