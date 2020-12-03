from queue import Queue


class Solution:
    def wordBreak(self, s, word_dict):
        q = Queue()
        q.put(0)
        n = len(s)
        visited = set()
        visited.add(0)

        while not q.empty():
            cur = q.get()
            for word in word_dict:
                w_len = len(word)
                if cur + w_len <= n and s[cur: cur+w_len] == word and cur + w_len not in visited:
                    if cur + w_len == n:
                        return True
                    visited.add(cur+w_len)
                    q.put(cur+w_len)
        return False


"""
s = 'leetcode', word_dict = ['leet', 'code']
q = [0], visited = {0}, n = 8
cur = 0
    word = 'leet', visited = {0, 4}, q = [4]
    word = 'code',
cur = 4
    word = 'leet'
    word = 'code'
"""

