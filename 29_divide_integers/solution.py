def divide(a, b):
    if a == -2147483648 and b == -1:
        return 2147483647
    if a == 0:
        return 0
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        sign = -1
    else:
        sign = 1

    res = 0
    a, b = abs(a), abs(b)

    while a >= b:
        p = b
        t = 1

        while (a >= (p << 2)):
            p = p << 1
            t = t << 1
        res += t
        a -= p
    return res if sign == 1 else -res


def divide_simple(a, b):
    res = 0
    while a >= b:
        p = b
        t = 1

        while (a >= p * 2):
            p *= 2
            t *= 2
        a -= p
        res += t

    return res

