def remove_parentheses(s):
    level = set()
    level.add(s)

    while True:
        res = []
        for e in level:
            if is_valid(e):
                res.append(e)

        if res:
            return res

        new_level = set()
        for e in level:
            for i in range(len(e)):
                new_level.add(e[:i]+e[i+1:])
        level = new_level


def is_valid(s):
    """
    check if the parentheses in s is valid
    """
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        elif c == ')':
            if cnt == 0:
                return False
            else:
                cnt -= 1

    return cnt == 0
