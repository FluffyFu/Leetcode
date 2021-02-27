from collections import deque


def min_cost(days, costs):
    """
    This version maintains each day in the calendar. It is easier to understand,
    but not very efficient
    """
    dp = [0] * 366
    i = 0
    for j in range(1, 366):
        if j < days[i]:
            dp[j] = dp[j-1]
        if j == days[i]:
            dp[j] = min((
                dp[j-1] + costs[0],
                dp[j-7] + costs[1] if j - 7 >= 0 else costs[1],
                dp[j-30] + costs[2] if j - 30 >= 0 else costs[2]
            ))
            i += 1
            if i == len(days):
                break
    return dp[days[-1]]


def min_cost2(days, costs):
    cost = 0

    # stores the (cost, date)
    last_7 = deque()
    last_30 = deque()

    for day in days:
        while last_7 and last_7[0][1] + 7 <= day:
            last_7.popleft()
        while last_30 and last_30[0][1] + 30 <= day:
            last_30.popleft()

        last_7.append((cost + costs[1], day))
        last_30.append((cost + costs[2], day))
        cost = min(last_7[0][0],
                   last_30[0][0],
                   cost + costs[0])
    return cost

