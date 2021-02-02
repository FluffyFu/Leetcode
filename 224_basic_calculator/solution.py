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
    for c in s+'+':
        if c.isdigit():
            cur = cur * 10 + int(c)
        elif c != ' ' and c != '(' and c != ')':
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
    s is the reserved.
    """
    opt = '+'
    stack = []
    cur = 0
    while len(s) > 0:
        c = s.pop()
        if c.isdigit():
            cur = cur * 10 + int(c)
        elif c == '(':
            cur = helper_2(s)
        elif c == ')':
            break
        elif c != ' ':
            if opt in ['+', '-']:
                sign = 1 if opt == '+' else -1
                stack.append(sign * cur)
            elif opt == '*':
                stack[-1] = stack[-1] * cur
            elif opt == '/':
                stack[-1] = int(stack[-1] / cur)
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

