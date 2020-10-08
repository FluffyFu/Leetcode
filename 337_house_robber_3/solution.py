from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        cache = {}
        return self._rob(root, cache)

    def _rob(self, root: TreeNode, cache) -> int:
        """
        The definition of this function is the maximum value when rob from the root.
        There are two cases based if the root is robbed.
            1. root is robbed, the result = root.val + root's grandchild if they exist.
            2. root is not robbed, the result = root's children's rob value.
        The final result the maximum of these two.
        """
        if not root:
            return 0
        if root in cache:
            return cache[root]
        c1 = self._rob(root.left, cache) + self._rob(root.right, cache)
        c2 = root.val
        if root.left:
            c2 += self._rob(root.left.left, cache)
            c2 += self._rob(root.left.right, cache)
        if root.right:
            c2 += self._rob(root.right.right, cache)
            c2 += self._rob(root.right.left, cache)

        cache[root] = max(c1, c2)
        return cache[root]

    def rob_2(self, root):
        return max(self._rob_2(root))

    def _rob_2(self, root) -> List[int]:
        """
        We can redefine the function such that it returns a list of two elements:
        the first value is with the root robbed, and the second value is with the
        root not robbed.
        """
        if not root:
            return [0, 0]
        left_vals = self._rob_2(root.left)
        right_vals = self._rob_2(root.right)

        # if we rob the current node, then it's left and
        # right child cannot be robbed.
        rob = root.val + left_vals[1] + right_vals[1]

        # if we don't rob the current node, we can choose if we want
        # to robber the left and right children based on the profit.
        not_rob = max(left_vals) + max(right_vals)

        return [rob, not_rob]

