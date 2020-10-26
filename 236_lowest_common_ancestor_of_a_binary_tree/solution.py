from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


class Solution2:
    """
    Iterative solution.
    """

    def lowestCommonAncestor(self, root, p, q):
        que = Queue()
        parents = {root: None}
        que.put(root)

        while not que.empty():
            cur = que.get()
            if cur.left:
                parents[cur.left] = cur
                que.put(cur.left)
            if cur.right:
                parents[cur.right] = cur
                que.put(cur.right)

        ancestor = set()
        while p:
            ancestor.add(p)
            p = parents[p]

        while q not in ancestor:
            q = parents[q]

        return q
