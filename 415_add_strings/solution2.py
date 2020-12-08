def add_str(num1, num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    res = []
    while i >= 0 or j >= 0:
        if i >= 0:
            n1 = int(num1[i])
        else:
            n1 = 0

        if j >= 0:
            n2 = int(num2[j])
        else:
            n2 = 0
        carry, cur = divmod(n1+n2+carry, 10)
        res.append(str(cur))

        i -= 1
        j -= 1

    if carry:
        res.append('1')

    return ''.join(res[::-1])

