def range_sum(root, low, high):
    if not root:
        return 0
    if root.val < low:
        return range_sum(root.right, low, high)
    if root.val > high:
        return range_sum(root.left, low, high)
    return root.val + range_sum(root.left, low, root.val) + range_sum(root.right, root.val, high)

