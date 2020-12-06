def overlap(A, B):
    if not A or not B:
        return []
    p1, p2 = 0, 0
    n1 = len(A)
    n2 = len(B)

    res = []
    while p1 < n1 and p2 < n2:
        l1, h1 = A[p1]
        l2, h2 = B[p2]

        if min(h1, h2) >= max(l1, l2):
            res.append([max(l1, l2), min(h1, h2)])

        if h1 > h2:
            p2 += 1
        elif h1 < h2:
            p1 += 1
        else:
            p1 += 1
            p2 += 1

    return res

