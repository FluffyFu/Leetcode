class Solution:
    """
    The backtracking method cause TLE error when the test case has the following
    format:
        s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        word_dict = {'a', 'aaa', 'aa', 'aaaa'}
    There are a lot of duplicated trees in the recursion process.
    """

    def word_break(self, s, word_dict):
        word_dict = set(word_dict)
        res = []
        record = []
        cache = {}
        self._back_tracking(s, 0, word_dict, res, record, cache)

        return res

    def _back_tracking(self, s, start, word_dict, res, record, cache):
        if start == len(s):
            res.append(" ".join(record))
            return
        for i in range(start+1, len(s)+1):
            if s[start:i] in word_dict:
                record.append(s[start:i])
                self._back_tracking(s, i, word_dict, res, record, cache)
                record.pop()


class Solution2:
    def word_break(self, s, word_dict):
        word_dict = set(word_dict)
        cache = dict()

        return self._word_break(s, 0, word_dict, cache)

    def _word_break(self, s, start, word_dict, cache):
        if start in cache:
            return cache[start]
        if start == len(s):
            return ['']
        res = []
        for i in range(start+1, len(s)+1):
            if s[start:i] in word_dict:
                res += [s[start:i] + ' ' + rest if rest else s[start:i]
                        for rest in self._word_break(s, i, word_dict, cache)]
        cache[start] = res
        return res
