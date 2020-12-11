def fractionToDecimal(numerator, denominator):
    if numerator == 0:
        return '0'
    res = []
    if numerator * denominator < 0:
        res.append('-')
    numerator, denominator = abs(numerator), abs(denominator)

    q, r = divmod(numerator, denominator)
    res.append(str(q))

    if r == 0:
        return ''.join(res)
    else:
        res.append('.')
    seen = dict()

    while r != 0 and r not in seen:
        seen[r] = len(res)
        q, r = divmod(r * 10, denominator)
        res.append(str(q))

    if r != 0:
        res.insert(seen[r], '(')
        res.append(')')

    return ''.join(res)

