def max_satisfied(customers, grumpy, X):

    cnts = 0
    for i in range(len(customers)):
        if i < X:
            cnts += customers[i]
        else:
            cnts += customers[i] * (1 - grumpy[i])

    l, r = 0, X
    res = cnts

    while r < len(grumpy):
        if grumpy[r] == 1:
            cnts += customers[r]
        if grumpy[l] == 1:
            cnts -= customers[l]

        res = max(res, cnts)

        l += 1
        r += 1

    return res

