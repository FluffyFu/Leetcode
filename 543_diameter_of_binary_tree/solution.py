class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        self._dfs(root, res)

        return res[0]

    def _dfs(self, root, res):
        if not root:
            return 0
        left = self._dfs(root.left, res)
        right = self._dfs(root.right, res)

        res[0] = max(left + right, res[0])

        return max(left+1, right+1)


"""
       1
      / \
     2   3
    / \
   4   5

dfs(1, [0])
    dfs(2, [0])
        dfs(4, [0])
            left = 0, right = 0, res = [1]
        done 4 left = 1

        dfs(5, [1])
            left = 0, right = 0, res = [1]
        done 5, right = 1

    res = [3]
    done 2 left = 2

    dfs(3, [3])
        left = 0, right = 0, res = [3]
    done 3 right = 1

done 1res = [4]
"""

