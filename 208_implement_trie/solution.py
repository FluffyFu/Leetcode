class Node:
    """
    Node object for implementing Trie.
    """
    R = 26  # radix

    def __init__(self, val=False):
        self._val = val
        self._next_nodes = [None for _ in range(self.R)]

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, value):
        self._val = value

    @property
    def next_nodes(self):
        return self._next_nodes


class Trie:
    def __init__(self):
        self._root = Node()

    def insert(self, word):
        self._root = self._insert(self._root, word, 0)

    def _insert(self, node, word, d):
        if not node:
            node = Node()
        if len(word) == d:
            node.val = True
            return node
        c = word[d]
        c_index = ord(c) - ord('a')
        node.next_nodes[c_index] = self._insert(
            node.next_nodes[c_index], word, d+1)
        return node

    def search(self, word):
        return self._search(self._root, word, 0)

    def _search(self, node, word, d):
        if not node:
            return False
        if len(word) == d:
            return node.val
        c = word[d]
        c_index = ord(c) - ord('a')
        return self._search(node.next_nodes[c_index], word, d+1)

    def startWith(self, prefix):
        return self._start_with(self._root, prefix, 0)

    def _start_with(self, node, word, d):
        if not node:
            return False
        if len(word) == d:
            return True
        c = word[d]
        c_index = ord(c) - ord('a')
        return self._start_with(node.next_nodes[c_index], word, d+1)
