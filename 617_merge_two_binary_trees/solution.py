
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None or t2 == None:
            return t1 if t2 == None else t2

        node = TreeNode(val=t1.val + t2.val)
        node.right = self.mergeTrees(t1.right, t2.right)
        node.left = self.mergeTrees(t1.left, t2.left)

        return node

