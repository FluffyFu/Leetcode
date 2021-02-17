def is_mon(A):
    if not A or len(A) <= 2:
        return True
    i = 1
    while i < len(A) and A[i-1] == A[i]:
        i += 1
    if i == len(A):
        return True
    elif A[i-1] < A[i]:
        for j in range(i, len(A)):
            if A[j-1] > A[j]:
                return False
    else:
        for j in range(i, len(A)):
            if A[j-1] < A[j]:
                return False
    return True


def is_mon_clean(A):
    res = set()
    for x, y in zip(A, A[1:]):
        if x != y:
            res.add(x > y)
    return len(res) <= 1

