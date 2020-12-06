def plus_one(digits):
    carry = 1
    res = []

    for d in digits[::-1]:
        carry, new_d = divmod(d + carry, 10)
        res.append(new_d)

    return res[::-1]

