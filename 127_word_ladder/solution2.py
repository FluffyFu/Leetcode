from queue import Queue


class Solution:
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    def ladder_length(self, begin_word, end_word, word_list):
        n = len(begin_word)

        q = Queue()
        word_list = set(word_list)
        visited = set()
        q.put(begin_word)
        visited.add(begin_word)

        step = 0
        while not q.empty():
            step += 1
            for _ in range(q.qsize()):
                cur = q.get()
                if cur == end_word:
                    return step
                for i in range(n):
                    for c in self.LETTERS:
                        candidate = cur[:i] + c + cur[i+1:]
                        if candidate in word_list and candidate not in visited:
                            visited.add(candidate)
                            q.put(candidate)
        return 0
