def sum_sub(A):
    """
    brutal force O(N**2)
    """
    res = 0

    for i in range(len(A)):
        cur_min = float('inf')
        for j in range(i, len(A)):
            cur_min = min(cur_min, A[j])
            res += cur_min
            res %= int(10**9 + 7)

    return res


def sum_sub_2(A):
    """
    The idea is that for the number A[i] find how many times it
    is used as the min. A[left] and A[right] are the first on the
    left and right that is smaller than A[i]. The number of times
    A[i] is used is (left + 1 - i + 1) * (right - i).

    Finding the first smaller element on the left and right can be done
    using a non-descreasing stack.
    """
    res = 0
    stack = []
    A.append(0)

    for i in range(len(A)):
        while stack and A[stack[-1]] > A[i]:
            cur = stack.pop()
            left = -1 if not stack else stack[-1]
            res += A[cur] * (cur - left) * (i - cur)
        stack.append(i)

    return res
