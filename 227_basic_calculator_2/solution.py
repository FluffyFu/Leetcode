def calculate(s):
    if not s:
        return 0
    s += '+0'
    cur = 0
    stack = []
    sign = '+'

    for c in s:
        if c.isdigit():
            cur = cur * 10 + int(c)
        elif not c.isspace():
            if sign == '+':
                stack.append(cur)
            elif sign == '-':
                stack.append(-cur)
            elif sign == '*':
                stack.append(stack.pop() * cur)
            elif sign == '/':
                temp = stack.pop()
                if temp // cur < 0 and temp % cur != 0:
                    stack.append(temp // cur + 1)
                else:
                    stack.append(temp // cur)
            sign = c
            cur = 0

    return sum(stack)

