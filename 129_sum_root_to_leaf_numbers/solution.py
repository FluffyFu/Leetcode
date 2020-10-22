class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        path = []
        self._sum_numbers(root, path, res)

        return sum(res)

    def _sum_numbers(self, root, path, res):
        if not root:
            return
        if (not root.left) and (not root.right):
            res.append(int(''.join(path + [str(root.val)])))
            return
        self._sum_numbers(root.left, path + [str(root.val)], res)
        self._sum_numbers(root.right, path + [str(root.val)], res)


"""
        4
       / \
      9    0
     / \
    5   1

_sum_numbers(4, [], [])
    _sum_numbers(9, ['4'], [])
        _sum_numbers(5, ['4', '9'], res)
            res = [495]
        5 done

        _sum_numbers(1, ['4, '9'], res)
            res = [495, 491]
        1 done
    9 done

    _sum_numbers(0, ['4'], res)
        res = [495, 491, 40]

    0 done
"""

