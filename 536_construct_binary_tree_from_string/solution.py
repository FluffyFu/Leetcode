class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s):
    return helper(s)


def helper(s):
    """
    Four cases:
        "",
        "243",
        "2(3)",
        "3(2)(4)"
    """
    ix = s.find('(')
    # takes care of the first two base cases
    if ix < 0:
        if s:
            return TreeNode(int(s))
        else:
            return None

    cnt = 0
    for j, c in enumerate(s):
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if j > ix and cnt == 0:
            break

    root = TreeNode(int(s[:ix]))
    # remove parenthesis of the left subtree
    root.left = helper(s[ix+1: j])
    # remove parenthesis of the right subtree (note the -1)
    root.right = helper(s[j+2: -1])


def stack_solution(s):
    if not s:
        return None
    i = 0
    # store unfinished nodes
    stack = []
    while i < len(s):
        if s[i] == ')':
            stack.pop()
        elif s[i] == '-' or s[i].isdigit():
            # menmerize int start position
            j = i
            while i+1 < len(s) and s[i+1].isdigit():
                i += 1
            # i is the last digit
            node = TreeNode(int(s[j:i+1]))
            i = j - 1
            if stack:
                top = stack[-1]
                if top.left:
                    top.right = node
                else:
                    top.left = node
            stack.append(node)
        i += 1

    return stack[0]

