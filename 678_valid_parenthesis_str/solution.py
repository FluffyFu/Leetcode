def valid(s):
    if not s:
        return True
    # number of left parenthesis that must be must be paired.
    # count every * as ).
    c_min = 0
    # number of left parenthesis that could be paired.
    c_max = 0

    for c in s:
        if c == '(':
            c_min += 1
            c_max += 1
        elif c == ')':
            c_min = max(c_min - 1, 0)
            c_max -= 1
        elif c == '*':
            c_min = max(c_min - 1, 0)
            c_max += 1

        if c_max < 0:
            return False
    return c_min == 0

