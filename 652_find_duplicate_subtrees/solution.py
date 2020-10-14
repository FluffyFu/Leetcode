# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_duplicate_subtrees(self, root):
        if not root:
            return []
        counter = dict()
        self._dfs(root, counter)

        res = []
        for cnt, node in counter.values():
            if cnt > 1:
                res.append(node)

        return res

    def _dfs(self, node, counter):
        if not node:
            return '#'
        s_left = self._dfs(node.left, counter)
        s_right = self._dfs(node.right, counter)
        s_node = str(node.val) + ',' + s_left + ',' + s_right

        if s_node in counter:
            counter[s_node] = (counter[s_node][0]+1, counter[s_node][1])
        else:
            counter[s_node] = (1, node)
        return s_node

