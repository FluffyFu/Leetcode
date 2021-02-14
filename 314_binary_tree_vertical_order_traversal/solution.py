from queue import Queue
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def v_order(root):
    if not root:
        return root
    c_map = defaultdict(list)
    col = 0

    q = Queue()
    q.put((root, col))

    while not q.empty():
        cur, col = q.get()
        c_map[col].append(cur)
        if cur.left:
            q.put((cur.left, col-1))
        if cur.right:
            q.put((cur.right, col+1))

    res = []
    for key in sorted(c_map.keys()):
        res.append([node.val for node in c_map[key]])

    return res

