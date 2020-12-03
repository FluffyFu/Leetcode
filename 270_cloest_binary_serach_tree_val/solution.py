class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def cloest_value(root, target):
    if not root:
        return None
    candidate = [root.val]
    dfs(root, target, candidate)
    return candidate[0]


def dfs(root, target, candidate):
    if not root:
        return
    if abs(root.val - target) < abs(candidate[0] - target):
        candidate[0] = root.val
    if root.val == target:
        candidate[0] = root.val
        return
    elif root.val > target:
        dfs(root.left, target, candidate)
    elif root.val < target:
        dfs(root.right, target, candidate)
