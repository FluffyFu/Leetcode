from collections import defaultdict
import bisect


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        """
        Time complexity O(m + n)
        """
        if not s:
            return True
        if not t:
            return False
        elif s[0] == t[0]:
            return self.is_subsequence(s[1:], t[1:])
        else:
            return self.is_subsequence(s, t[1:])

    def is_subsequence_iterative(self, s: str, t: str) -> bool:
        """
        Time complexity O(m + n)
        """
        if not s:
            return True
        if not t:
            return False

        index_s = 0
        index_t = 0

        n_s = len(s)
        n_t = len(t)

        while index_t < n_t and index_s < n_s:
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1

        return index_s == n_s

    def is_subsequence_iterative_clean(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)

    def is_subsequence_streaming(self, s: str, t: str) -> bool:
        """
        We have a fixed t and a stream of s. Solve the problem under this
        scenario.
        """
        index_map = defaultdict(list)

        for i, c in enumerate(t):
            index_map[c].append(i)

        index = 0  # keep track of the current index in t
        for c in s:
            if c not in index_map:
                return False
            else:
                j = bisect.bisect_left(index_map[c], index)
                if j == len(index_map[c]):
                    return False
                else:
                    index = index_map[c][j] + 1

        return True

