def regex(s, p):
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

    # s = '', p = ''
    dp[0][0] = True

    # s = '', loop p
    for i in range(1, len(p)+1):
        if p[i-1] == '*':
            dp[i][0] = (i == 1 or dp[i-2][0])

    for i in range(1, len(p) + 1):
        for j in range(1, len(s)+1):
            if p[i-1] != '*':
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
            else:
                # when p[i-1] is '*' there are two cases:
                # vertical
                # 1. keep as dp[i-1][j], treat * as 1 rep.
                # 2. keep as dp[i-2][j], treat * as 0 rep, eliminate the
                # previous char
                dp[i][j] = dp[i-1][j] or (i > 1 and dp[i-2][j])

                # horizontal
                # if vertical does not work out, we still have chance to
                # match by having * as repeating the previous letter
                if p[i-2] == s[j-1] or p[i-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i][j-1]

    return dp[-1][-1]

