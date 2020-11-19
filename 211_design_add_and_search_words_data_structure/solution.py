from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self._table = defaultdict(set)

    def addWord(self, word):
        self._table[len(word)].add(word)

    def search(self, word):
        if len(word) not in self._table:
            return False
        for target in self._table[len(word)]:
            if self._is_match(word, target):
                return True

        return False

    def _is_match(self, w1, w2):
        """
        w1 and w2 should have the same length.
        """
        for i in range(len(w1)):
            if w1[i] != w2[i] and w1[i] != '.' and w2[i] != '.':
                return False
        return True


"""
self._table = {3: {'bad', 'dad', 'mad'}}
search('pad')
search('.ad'), w1 = '.ad', w2 = 'bad'
"""

