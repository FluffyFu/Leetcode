def min_cost(arr):
    n = len(arr)
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        # dp[i][i] = arr[i]
        dp[i][i] = 0

    for d in range(1, n):
        for i in range(n):
            j = i + d
            if j > n - 1:
                break
            res = float('inf')
            for k in range(i, j):
                val = dp[i][k] + dp[k+1][j] + \
                    max(arr[i:k+1]) * max(arr[k+1:j+1])
                res = min(res, val)
            dp[i][j] = res

    return dp[0][n-1]


def min_cost_2(nums):
    res = 0
    # mono non-increasing stack
    stack = [float('inf')]

    for a in nums:
        while stack[-1] <= a:
            mid = stack.pop()
            # find the smaller one from left and right neighbor
            res += mid * min(a, stack[-1])
        stack.append(a)

    # deal with elements in the stack
    while len(stack) >= 3:
        res += stack.pop() * stack[-1]

    return res

