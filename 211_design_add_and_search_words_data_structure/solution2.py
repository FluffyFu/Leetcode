from collections import defaultdict


class Node:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = defaultdict(Node)


class WordDictionary:
    def __init__(self):
        self._root = Node()

    def addWord(self, word):
        current = self._root
        for c in word:
            current = current.children[c]

        current.is_word = True

    def search(self, word):
        return self._search(self._root, word, 0)

    def _search(self, node, word, d):
        if not node:
            return False
        if len(word) == d:
            return node.is_word
        c = word[d]
        if c == '.':
            for child in node.children.values():
                if self._search(child, word, d+1):
                    return True
            return False
        else:
            return self._search(node.children[c], word, d+1)

