from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_complete(root):
        res = [root]
        i = 0

        while res[i]:
            res.append(res[i].left)
            res.append(res[i].right)
            i += 1

        return not any(res[i:])
