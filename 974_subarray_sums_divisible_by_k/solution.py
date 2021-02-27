from collections import defaultdict


def n_valid(A, k):
    """
    TLE, O(N**2)
    """
    c_sum = [0]
    for a in A:
        c_sum.append(c_sum[-1] + a)
    res = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)+1):
            if (c_sum[j] - c_sum[i]) % k == 0:
                res += 1

    return res


def n_valid2(A, k):
    c_sum = [0]
    for a in A:
        c_sum.append(c_sum[-1] + a)

    res = 0
    table = defaultdict(int)
    for i in range(len(c_sum)):
        t = c_sum[i] % k
        res += table[t]
        table[t] += 1

    return res

