class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def diameter(root):
    res = [0]
    height(root, res)

    return res[0]


def height(root, res):
    if not root:
        return 0

    max1 = 0
    max2 = 0

    for child in root.children:
        h = height(child, res)
        if h > max1:
            max2 = max1
            max1 = h
        elif h > max2:
            max2 = h

        res[0] = max(res[0], max1 + max2)

    return max1 + 1  # 1 accounts for the current node

