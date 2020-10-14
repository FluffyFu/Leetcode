from queue import Queue


class Solution:
    def word_break(self, s, word_dict):
        res = []
        cache = {}
        word_dict = set(word_dict)
        self._word_break(s, word_dict, res, cache)

        return res != []

    def _word_break(self, s, word_dict, res, cache):
        """
        Very similar to backtracking, but we only need to find one valid result.
        Use a dictionary to cache the searched trees
        """
        if s == '':
            res.append(1)
            return
        if s in cache:
            if cache[s] == 1:
                res.append[1]
            return
        for i in range(len(s) + 1):
            if s[:i] in word_dict:
                self._word_break(s[i:], word_dict, res, cache)
            if res:
                cache[s] = 1
                return
        cache[s] = 0


class Solution_2:
    def word_break(self, s, word_dict):
        cache = set()
        word_dict = set(word_dict)

        return self._dfs_1(s, 0, word_dict, cache)

    def _dfs_1(self, s, start, word_dict, visited):
        """
        View this as a graph problem. Each index is a vertex. We try to find
        out if it is possible to find a path from 0 to len(s). Depending on how
        to iterate through the neighbors, dfs can run in two versions

        1. loop through all the possible index and if it is possible to reach that index, continue doing dfs.

        2. loop through the dict and find out the reachable index and perform dfs from there.
        """
        if start == len(s):
            return True
        for i in range(start+1, len(s) + 1):
            if i not in visited and s[start:i] in word_dict:
                visited.add(i)
                if self._dfs_1(s, i, word_dict, visited):
                    return True
        return False

    def _dfs_2(self, s, start, word_dict, visited):
        if start == len(s):
            return True
        for w in word_dict:
            if (len(w) + start <= len(s)) and (s[start:len(w) + start] == w) and ((start + len(w)) not in visited):
                if self._dfs_1(s, start + len(w), word_dict, visited):
                    return True
                visited.add(len(w) + start)
        return False


class Solution_3:
    """
    Since this can be viewed as a graph problem. BFS is another option.
    """

    def word_break(self, s, word_dict):
        visited = set()
        q = Queue()
        q.put(0)

        while not q.empty():
            cur = q.get()
            if cur == len(s):
                return True

            for w in word_dict:
                v = cur + len(w)
                if v <= len(s) and v not in visited and w == s[cur:v]:
                    q.put(v)
                    visited.add(v)

        return False

    def word_break_2(self, s, word_dict):
        """
        This solution works fine.
        """
        visited = set()
        q = Queue()
        q.put(0)
        word_dict = set(word_dict)

        while not q.empty():
            cur = q.get()
            if cur == len(s):
                return True

            for j in range(cur+1, len(s) + 1):
                if s[cur:j] in word_dict and j not in visited:
                    q.put(j)
                    visited.add(j)

        return False


class Solution_4:
    def word_break(self, s, word_dict):
        """
        DP method. dp[i] means if s[:i] can be broken.
        The update rule is:
        dp[i+1] = any(dp[j] and s[j:i+1] in word_dict for j in range(i+1))
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j: i] in word_dict for j in range(i))
        return dp[-1]
