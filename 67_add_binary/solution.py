def add_binary(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0

    res = []
    while i >= 0 or j >= 0:
        if i >= 0:
            n1 = int(a[i])
        else:
            n1 = 0
        if j >= 0:
            n2 = int(b[j])
        else:
            n2 = 0

        carry, cur = divmod(n1+n2+carry, 2)
        res.append(str(cur))
        i -= 1
        j -= 1

    if carry:
        res.append(str(carry))

    return ''.join(res[::-1])

