def cal(s):
    return helper_2(list(s[::-1]))


def helper(s):
    """
    Calculate the result without parenthesis.
    """
    opt = '+'
    stack = []
    cur = 0
    # add an extra opt in the end to trigger the last operation.
    for i, c in enumerate(s):
        if c.isdigit():
            cur = cur * 10 + int(c)
        # make sure the last operation is performed.
        if c != ' ' or i == len(s) - 1:
            if opt in ['+', '-']:
                sign = 1 if opt == '+' else -1
                stack.append(cur * sign)
            elif opt == '*':
                stack[-1] = stack[-1] * cur
            elif opt == '/':
                stack[-1] = int(stack[-1] / cur)
            opt = c
            cur = 0
    return sum(stack)


def helper_2(s):
    """
    There are a few tricks in here:

    1. Don't forget the last operation. (when len(s) == 0 and come across
     ')'). This is why we are using if instead of elif.
    2. Since we are using recursive call here, we need to modify
    the original list, otherwise we cannot keep track of where we are.
    """
    opt = '+'
    stack = []
    cur = 0
    while len(s) > 0:
        c = s.pop()
        if c.isdigit():
            cur = cur * 10 + int(c)
        if c == '(':
            cur = helper_2(s)
        if c in ['+', '-', '*', '/', ')'] or len(s) == 0:
            if opt in ['+', '-']:
                sign = 1 if opt == '+' else -1
                stack.append(sign * cur)
            elif opt == '*':
                stack[-1] = stack[-1] * cur
            elif opt == '/':
                stack[-1] = int(stack[-1] / cur)
            opt = c
            cur = 0
        if c == ')':
            break
    return sum(stack)


def simple(s):
    """
    s only contains + and - operations and does not have parenthesis.
    """
    res = 0
    sign = 1
    cur = 0

    for c in s:
        if c in ['+', '-']:
            res += sign * cur
            sign = 1 if c == '+' else -1
            cur = 0
        elif c.isdigit():
            cur = cur * 10 + int(c)
    res += cur * sign
    return res

