class Solution:
    def is_alien_sorted(self, words, order):
        mapping = dict()
        normal_order = 'abcdefghijklmnopqrstuvwxyz'
        for new, normal in zip(order, normal_order):
            mapping[new] = normal

        noraml_words = []
        for w in words:
            res = []
            for c in w:
                res.append(mapping[c])
            noraml_words.append(''.join(res))

        for i in range(len(noraml_words) - 1):
            if noraml_words[i] > noraml_words[i+1]:
                return False

        return True

