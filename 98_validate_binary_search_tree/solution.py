from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Flatten the tree using in-order traversal and check if the array is sorted.
    """

    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        self._in_order_traversal(root, result)

        if len(result) < 2:
            return True
        for i in range(len(result) - 1):
            if result[i] >= result[i+1]:
                return False
        return True

    def _in_order_traversal(self, node: TreeNode, result: List[int]):
        if not node:
            return
        self._in_order_traversal(node.left, result)
        result.append(node.val)
        self._in_order_traversal(node.right, result)


class SolutionTopDown:
    """
    Given the parent node, the range of left and right subtrees can be specified.
    """

    def isValidBST(self, root: TreeNode) -> bool:
        low = float('-inf')
        high = float('inf')

        return self._validate(root, low, high)

    def _validate(self, root: TreeNode, low: float, high: float) -> bool:
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        return self._validate(root.left, low, root.val) and self._validate(root.right, root.val, high)

