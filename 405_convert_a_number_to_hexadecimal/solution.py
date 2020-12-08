def convert(num):
    if num == 0:
        return '0'
    if num < 0:
        num += 1 << 32
    res = []
    c_map = '0123456789abcdef'

    while num > 0:
        num, r = divmod(num, 16)
        res.append(c_map[r])

    return ''.join(res[::-1])

