class Solution:
    def max_evelopes(self, envelopes):
        if not envelopes:
            return 0

        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))

        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            max_len = 1
            for j in range(0, i):
                if envelopes[j][1] < envelopes[i][1]:
                    max_len = max(dp[j] + 1, max_len)

            dp[i] = max_len

        return max(dp)
