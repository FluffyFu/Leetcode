def job_schedule(startTime, endTime, profit):
    jobs = sorted(list(zip(startTime, endTime, profit)), key=lambda x: x[1])

    dp = [(0, 0)]  # the max profit at time t, (t, max_profit)
    for s, e, p in jobs:
        # find the latest time point when the current job is feasible.
        pre_p = find_left(dp, s)
        if pre_p + p > dp[-1][1]:
            dp.append((e, pre_p + p))

    return dp[-1][1]


def find_left(dp, start):
    """
    Find the profit corresponding to the latest time that is smaller than the given
    start time.
    """
    l = 0
    r = len(dp) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if dp[mid][0] < start:
            l = mid + 1
        elif dp[mid][0] > start:
            r = mid - 1
        else:
            return dp[mid][1]

    # l is where the start should be inserted
    # there are two cases (equal to start has already been taken care of):
    if l == len(dp):
        # start is larger than all the values
        return dp[-1][1]
    elif dp[l][0] > start:
        # start is smaller than dp[l][0], return the previous one
        return dp[l-1][1]

