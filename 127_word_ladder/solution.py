from typing import List, Dict, Set
from queue import Queue


class Solution:
    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if not word_list:
            return 0
        graph = self._build_graph(list(word_list), begin_word)
        visited = set()
        q = Queue()
        q.put(begin_word)

        distance = 0
        while not q.empty():
            level_len = q.qsize()

            for _ in range(level_len):
                current = q.get()
                visited.add(current)
                if current == end_word:
                    return distance + 1
                for w in graph[current]:
                    if not w in visited:
                        q.put(w)
            distance += 1
        return 0

    def _build_graph(self, word_list: List[str], begin_word: str) -> Dict[str, List[str]]:
        """
        Internal function to build a graph from the given list. If two words only differs by one letter,
        there is a edge between them.
        """
        if not begin_word in word_list:
            word_list.append(begin_word)
        res = {w: [] for w in word_list}
        for w1 in word_list:
            for w2 in word_list:
                if (w1 != w2) and self._is_valid(w1, w2):
                    res[w1].append(w2)

        return res

    def _is_valid(self, w1: str, w2: str):
        """
        Check is w1 and w2 only differ by one letter. Assume w1 and w2 has the same length.
        """
        n = 0

        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                n += 1

            if n >= 2:
                return False

        return True if n == 1 else False
