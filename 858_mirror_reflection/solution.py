def relfection(p, q):
    lcm = p // gcd(p, q) * q

    n_v = lcm / p
    n_h = lcm / q

    if n_h % 2 == 0:
        return 2
    else:
        return 1 if n_v % 2 == 1 else 0


def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)
