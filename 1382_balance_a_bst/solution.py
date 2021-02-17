class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance(root):
    if not root:
        return None
    nums = []
    inorder(root, nums)
    return build_bst(nums)


def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)


def build_bst(nums):
    if not nums:
        return None
    mid_index = len(nums)//2
    mid = nums[mid_index]

    root = TreeNode(mid)
    root.left = build_bst(nums[:mid_index])
    root.right = build_bst(nums[mid_index+1:])

    return root
