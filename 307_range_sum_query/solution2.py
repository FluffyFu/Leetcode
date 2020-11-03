class Node:
    def __init__(self, start, end, total=None, left=None, right=None):
        self.start = start
        self.end = end
        self.total = total
        self.left = left
        self.right = right


class NumArray:
    """
    Use segment tree data structure to achieve O(log(n)) update and
    range sum time complexity.
    """

    def __init__(self, nums):
        self._tree = self._construct_segment_tree(nums, 0, len(nums)-1)

    def update(self, i, val):
        self._update_segment_tree(self._tree, i, val)

    def sumRange(self, i, j):
        return self._cal_range_sum(self._tree, i, j)

    def _construct_segment_tree(self, nums, l, r):
        if l > r:
            return None
        if l == r:
            root = Node(l, r, nums[l])
            return root
        root = Node(l, r)
        mid = l + (r - l) // 2
        root.left = self._construct_segment_tree(nums, l, mid)
        root.right = self._construct_segment_tree(nums, mid+1, r)
        root.total = root.left.total + root.right.total

        return root

    def _update_segment_tree(self, root, i, val):
        if root.start == root.end:
            root.total = val
            return
        mid = (root.start + root.end) // 2
        if i <= mid:
            self._update_segment_tree(root.left, i, val)
        else:
            self._update_segment_tree(root.right, i, val)

        root.total = root.left.total + root.right.total

    def _cal_range_sum(self, root, l, r):
        if root.start == l and root.end == r:
            return root.total

        mid = (root.start + root.end) // 2
        if mid < l:
            return self._cal_range_sum(root.right, l, r)
        elif mid >= l and mid < r:
            return self._cal_range_sum(root.left, l, mid) + self._cal_range_sum(root.right, mid+1, r)
        elif mid >= r:
            return self._cal_range_sum(root.left, l, r)

