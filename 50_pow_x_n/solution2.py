def pow(x, n):
    if n == 0:
        return 1
    cache = dict()
    if n < 0:
        return 1 / pow_internal(x, -n, cache)
    else:
        return pow_internal(x, n, cache)


def pow_internal(x, n, cache):
    if n in cache:
        return cache[n]
    if n == 1:
        return x
    if n % 2 == 0:
        res = pow_internal(x, n/2, cache) ** 2
        cache[n] = res
        return res
    else:
        res = x * pow_internal(x, n-1, cache)
        cache[n] = res
        return res
