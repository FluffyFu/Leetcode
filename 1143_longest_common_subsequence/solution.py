class Solution:
    def longest_common_subsequence(self, text1, text2):
        # dp[i][j] is the LCS between text1[:i] and text2[:j]
        dp = [[0 for _ in range(len(text2) + 1)]
              for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]


class Solution2:
    def longest_common_subsequence_recursive(self, text1, text2):
        cache = dict()
        return self.helper(text1, len(text1)-1, text2, len(text2)-1, cache)

    def helper(self, text1, end1, text2, end2, cache):
        if (end1, end2) in cache:
            return cache[(end1, end2)]
        if end1 == -1 or end2 == -1:
            return 0
        if text1[end1] == text2[end2]:
            res = self.helper(text1, end1-1, text2, end2-1, cache) + 1
            cache[(end1, end2)] = res
            return res
        else:
            res = max(self.helper(text1, end1-1, text2, end2, cache),
                      self.helper(text1, end1, text2, end2-1, cache))
            cache[(end1, end2)] = res
            return res


"""
t1 = 'abcde', t2 = 'ace'
dp =
   0 0 0 0
   0 1 1 1
   0 1 1 1
   0 1 2 2
   0 1 2 2
   0 2 2 3
i = 1, j = 1
i = 1, j = 2, a != c
i = 1, j = 3, a != e
i = 2, j = 1, b != a
i = 2, j = 2, b != c
i = 2, j =3, b != e
i = 3, j = 1, c != a
i = 3, j = 2, c == c
i = 3, j = 3, c != e
i = 4, j = 1, d != a
i = 4, j = 2, d != c
i = 4, j = 3, d != e
i = 5, j = 1, e != a
i = 5, j = 2, e != c
i = 5, j = 3, e == e


"""
