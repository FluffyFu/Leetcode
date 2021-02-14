class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(t):
    if not t:
        return ''
    s_root = str(t.val)
    if t.left:
        s_root += '(' + tree2str(t.left) + ')'
    if not t.left and t.right:
        s_root += '()'
    if t.right:
        s_root += '(' + tree2str(t.right) + ')'
    return s_root

