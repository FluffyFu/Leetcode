class Solution:
    def word_break(self, s, word_dict):
        res = []
        cache = {}
        word_dict = set(word_dict)
        self._word_break(s, word_dict, res)

        return res != []

    def _word_break(self, s, word_dict, res, cache):
        if s == '':
            res.append(1)
            return
        if s in cache:
            if cache[s] == 1:
                res.append[1]
            return
        for i in range(len(s) + 1):
            if s[:i] in word_dict:
                res = self._word_break(s[i:], word_dict, res, cache)
                cache[s[i:]] = res


"""
s = 'abe', word_dict = {'be', 'a'}

word_break('abe', word_dict)
    word_break('be', word_dict)
        return True

    return True


"""
