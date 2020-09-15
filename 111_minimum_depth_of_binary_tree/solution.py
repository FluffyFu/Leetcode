
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self._min_depth(root)

    def _min_depth(self, node: TreeNode) -> int:
        if node == None:
            return 0
        if node.left == None:
            # only node with leaf is eligible for depth counting.
            return self._min_depth(node.right) + 1
        elif node.right == None:
            return self._min_depth(node.left) + 1
        else:
            return min(self._min_depth(node.left), self._min_depth(node.right)) + 1

    def _min_depth_2(self, node: TreeNode) -> int:
        if node == None:
            return 0
        d_right = self._min_depth_2(node.right)
        d_left = self._min_depth_2(node.left)

        # if d_left > 0 and d_right > 0, return the smaller one,
        # otherwise return the larger one.
        return 1 + (min(d_left, d_right) or max(d_left, d_right))
