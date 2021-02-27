def backspace(S, T):
    s = clean(S)
    t = clean(T)

    return s == t


def clean(s):
    stack = []

    for c in s:
        if c == '#':
            if stack:
                stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)
