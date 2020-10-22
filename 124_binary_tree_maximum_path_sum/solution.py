class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [-float('inf')]
        self._max_path_sum(root, res)
        return res[0]

    def _max_path_sum(self, root, res):
        """
        Returns the max sum between the left and right subtree.
        """
        if not root:
            return 0
        left_sum = max(self._max_path_sum(root.left, res), 0)
        right_sum = max(self._max_path_sum(root.right, res), 0)

        res[0] = max(root.val + left_sum + right_sum, res[0])

        return root.val + max(left_sum, right_sum)

