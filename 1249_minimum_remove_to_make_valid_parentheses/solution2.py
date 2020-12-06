def remove_parans(s):
    s = list(s)
    invalid_index = []
    n_left = []

    for i, c in enumerate(s):
        if c == '(':
            n_left.append(i)
        elif c == ')':
            if len(n_left) == 0:
                invalid_index.append(i)
            else:
                n_left.pop()

    invalid_index += n_left
    invalid_index = set(invalid_index)

    res = []
    for i in range(len(s)):
        if i not in invalid_index:
            res.append(s[i])

    return ''.join(res)

