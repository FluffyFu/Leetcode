class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    stack = []
    node = root
    res = []

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        cur = stack.pop()
        res.append(cur.val)
        node = cur.right
    return res


def inorder_dfs(node):
    if not node:
        return []
    left = inorder(node.left)
    right = inorder(node.right)

    return left + [node.val] + right


def convert(root):
    """
    Use stack to do inorder traversal and maintain pre and cur node.
    Do two operations: pre.right = cur and cur.left = pre.

    In the end attach the front and end.
    """
    if not root:
        return root

    stack = []
    node = root
    dummy = Node(0)
    pre = dummy

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        cur = stack.pop()

        cur.left = pre
        pre.right = cur
        pre = cur

        node = cur.right

    cur.right = dummy.right
    dummy.right.left = cur

    return dummy.right

