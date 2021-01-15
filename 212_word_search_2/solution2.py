from collections import defaultdict


class TrieNode:
    def __init__(self, val=False):
        self.val = val
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.val = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            if not node:
                return False
        return node.val


def search(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    # backtracking
    res = []
    node = trie.root
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, board, node, '', res)
    return res


def dfs(i, j, board, node, path, res):
    if node.val:
        res.append(path)
        node.val = False
    if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
        return
    tmp = board[i][j]
    node = node.children.get(tmp)
    if not node:
        return
    board[i][j] = '*'
    dfs(i+1, j, board, node, path+tmp, res)
    dfs(i-1, j, board, node, path+tmp, res)
    dfs(i, j-1, board, node, path+tmp, res)
    dfs(i, j+1, board, node, path+tmp, res)
    board[i][j] = tmp

