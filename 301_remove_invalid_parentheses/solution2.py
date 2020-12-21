def remove_parentheses(s):
    level = {s}

    while True:
        res = []
        for cur in level:
            if is_valid(cur):
                res.append(cur)
        if res:
            return res

        new_level = set()
        for cur in level:
            for i in range(len(cur)):
                new_level.add(cur[:i] + cur[i+1:])

        level = new_level


def is_valid(s):
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
