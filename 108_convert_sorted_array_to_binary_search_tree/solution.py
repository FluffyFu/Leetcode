from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = int(len(nums) / 2)

        mid_val = nums[mid]
        left_nums = nums[:mid]
        right_nums = nums[mid+1:]

        node = TreeNode(val=mid_val)
        node.left = self.sortedArrayToBST(left_nums)
        node.right = self.sortedArrayToBST(right_nums)

        return node


class SolutionNoSlicing:
    """
    Avoid array slicing.
    """

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._convert(0, len(nums)-1, nums)

    def _convert(self, left: int, right: int, nums) -> TreeNode:
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])
        node.left = self._convert(left, mid-1, nums)
        node.right = self._convert(mid+1, right, nums)

        return node

