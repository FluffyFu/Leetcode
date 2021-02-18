def longest_palindrome_substring(s):
    if not s or len(s) == 1:
        return s

    # dp[i][j] stores if s[i:j+1] is palindrome.
    res = s[0]
    max_len = 1
    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True
        if i != 0:
            dp[i][i-1] = True

    for i in range(len(s)-2, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j] and dp[i+1][j-1]:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    res = s[i:j+1]
                dp[i][j] = True
            else:
                dp[i][j] = False
    return res

