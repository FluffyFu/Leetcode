from collections import Counter
import heapq


class Word:
    def __init__(self, w, c):
        self.w = w
        self.c = c

    def __lt__(self, other):
        if self.c < other.c:
            return True
        elif self.c == other.c:
            return self.w > other.w
        else:
            return False

    def __eq__(self, other):
        return self.c == other.c and self.w == other.w


def top_frequent(words, k):

    cnt = Counter(words)

    hq = []
    for w, v in cnt.items():
        heapq.heappush(hq, Word(w, v))
        if len(hq) > k:
            heapq.heappop(hq)

    res = []
    while hq:
        res.append(heapq.heappop(hq).w)

    return res[::-1]

