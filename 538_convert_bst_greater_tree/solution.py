class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convert_bst(self, root: TreeNode) -> TreeNode:
        self._dfs(root, [0])

    def _dfs(self, root, current_sum):
        if not root:
            return
        self._dfs(root.right, current_sum)
        current_sum[0] += root.val
        root.val = current_sum[0]
        self._dfs(root.left, current_sum)


"""
                    30 
                   / \
                  36   21
                 / |  | \
               36   35  26   15
                   \       \
                    33      8
dfs(4, [0])
    dfs(6, [0])
        dfs(7, [0])
            dfs(8, [0])
            current_sum = [8]
            8 done
        current_sum = [15]
        7 done
    current_sum = [21]
        dfs(5, [21])
        current_sum = [26]
    6 done
    current_sum = [30]

    dfs(1, [30])
        dfs(2, [30])
            dfs(3, [30])
                current_sum = [33]
            3 done
            current_sum = [35]

        2 done
        dfs(0, [30])




"""

