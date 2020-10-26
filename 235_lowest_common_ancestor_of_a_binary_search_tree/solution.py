from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        que = Queue()
        que.put(root)

        while not que.empty():
            cur = que.get()
            if cur.val == p.val or cur.val == q.val:
                return cur
            elif cur.val > p.val and cur.val > q.val:
                que.put(cur.left)
            elif cur.val < p.val and cur.val < q.val:
                que.put(cur.right)
            else:
                return cur

    def lowest_common_ancestor_clean(self, root, p, q):

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


"""
p = 2, q = 8
que = [6]
cur = 6, que = [2]
cur = 2, return 2


que = [6], p = 2, q = 8
cur = 6 return 6
"""

