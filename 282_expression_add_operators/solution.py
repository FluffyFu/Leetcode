def add_ops(num, target):
    res = []
    # this for loop takes care of the corner case we start with
    # empty expression, exp is a number instead of operator + num
    for i in range(1, len(num)+1):
        if i == 1 or (i > 1 and num[0] != '0'):
            # This makes sure the value does not start with 0
            dfs(num[i:], str(num[:i]), int(num[:i]),
                int(num[:i]), res, target)
    return res


def dfs(num, exp, cur_val, last_val, res, target):
    if not num and cur_val == target:
        res.append(exp)
        return

    for i in range(1, len(num)+1):
        if i == 1 or (i > 1 and num[0] != '0'):
            val = int(num[:i])
            dfs(num[i:], exp + '+' + str(val), cur_val + val, val, res, target)
            dfs(num[i:], exp + '-' + str(val),
                cur_val - val, -val, res, target)
            dfs(num[i:], exp + '*' + str(val), cur_val - last_val +
                last_val * val, last_val * val, res, target)
