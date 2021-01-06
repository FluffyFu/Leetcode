def min_swaps(data):
    n_ones = sum(data)

    n_zeros = n_ones - sum(data[:n_ones])
    res = n_zeros

    r = n_ones
    l = 0

    while r < len(data):
        if data[r] == 0:
            n_zeros += 1
        if data[l] == 0:
            n_zeros -= 1

        res = min(n_zeros, res)

        r += 1
        l += 1

    return res

