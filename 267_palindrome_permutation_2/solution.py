from collections import Counter


class Solution:
    def generate_palindromes(self, s):
        # check if it is possible to form a palindrome
        c = Counter(s)
        if sum(1 for val in c.values() if val % 2 == 1) > 1:
            return []
        else:
            res = []
            path = []
            self._back_tracking(Counter(s), path, res)
            return res

    def _back_tracking(self, counter, path, res):
        if sum(counter.values()) == 0:
            res.append(''.join(path) + ''.join(path[::-1]))
            return
        if sum(counter.values()) == 1:
            for c, cnt in counter.items():
                if cnt == 1:
                    res.append(''.join(path) + c + ''.join(path[::-1]))
                    return
        for c, cnt in counter.items():
            if cnt == 1:
                continue
            if cnt != 0:
                path.append(c)
                counter[c] -= 2
                self._back_tracking(counter, path, res)
                counter[c] += 2
                path.pop()

