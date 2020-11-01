class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        self.in_order(root, res, k)

        return res[-1]

    def in_order(self, root, res, k):
        if not root:
            return
        if len(res) == k:
            return
        self.in_order(root.left, res, k)
        if len(res) < k:
            res.append(root.val)
        else:
            return
        self.in_order(root.right, res, k)


"""
       5
      / \
     3   6
    / \
   2   4
   /
  1
res = [], k = 3

in_order(5, [])
    in_oder(3, [])
        in_order(2, [])
            in_order(1, [])
                res = [1]
            1 done
            res = [1, 2]
        2 done
        res = [1, 2, 3]
        in_order(4, [1, 2, 3])
        4 done
    3 done
5 done
"""

