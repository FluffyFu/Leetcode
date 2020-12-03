class Solution:
    def wordBreak(self, s, word_dict):
        res = []
        self.back_track(0, res, [], word_dict, s, len(s))
        return res

    def back_track(self, start, res, track, word_dict, s, n):
        if start == n:
            res.append(' '.join(track))
            return

        for word in word_dict:
            w_len = len(word)
            if start + w_len <= n and s[start: start + w_len] == word:
                self.back_track(start + w_len, res, track +
                                [word], word_dict, s, n)

