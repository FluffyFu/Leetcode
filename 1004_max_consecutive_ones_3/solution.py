def max_ones(A, K):
    """
    Intuition: find the longest subarray contains at most K zeros
    """
    i = 0
    for j in range(len(A)):
        if A[j] == 0:
            K -= 1

        if K < 0:
            if A[i] == 0:
                K += 1
            i += 1
    return j - i + 1


def max_ones_2(A, K):
    res = 0
    slow = 0
    fast = 0

    while fast < len(A):
        if A[fast] == 0:
            K -= 1

        if K < 0:
            while K < 0:
                if A[slow] == 0:
                    K += 1

                slow += 1
        res = max(res, fast - slow + 1)
        fast += 1

    return res

