def longest_common_subsequence(text1, text2):
    if not text1 or not text2:
        return 0

    n1 = len(text1)
    n2 = len(text2)

    # dp[i][j] is the LCS of text1[:i], text1[:j]

    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

