def valid(s):
    if not s:
        return True
    left_c = 0
    res = 0

    for c in s:
        if c == '(':
            left_c += 1
        elif c == ')':
            if left_c > 0:
                left_c -= 1
            else:
                res += 1
    return res + left_c

