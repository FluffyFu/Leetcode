def cal(s):
    return helper(list(s[::-1]))


def helper(s):
    """
    s is reverse list of the original string.
    """
    cur = 0
    op = '+'
    stack = []

    while s:
        c = s.pop()

        if c.isdigit():
            cur = cur * 10 + int(c)
        if c == '(':
            cur = helper(s)
        if c in ['+', '-', '*', '/', ')'] or not s:
            if op in ['+', '-']:
                sign = 1 if op == '+' else -1
                stack.append(sign * cur)
            elif op == '*':
                stack[-1] = stack[-1] * cur
            elif op == '/':
                stack[-1] = int(stack[-1] / cur)
            op = c
            cur = 0
        if c == ')':
            break
    return sum(stack)
