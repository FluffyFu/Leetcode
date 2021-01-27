def sum_sub(A):
    res = 0

    for i in range(len(A)):
        cur_min = float('inf')
        for j in range(i, len(A)):
            cur_min = min(cur_min, A[j])
            res += cur_min
            res %= int(10**9 + 7)

    return res

