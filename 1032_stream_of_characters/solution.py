from collections import deque


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.waitlist = []
        for w in words:
            temp_dict = self.trie
            for c in w:
                temp_dict = temp_dict.setdefault(c, dict())
            temp_dict['#'] = '#'

    def query(self, letter: str) -> bool:
        waitlist = []

        if letter in self.trie:
            waitlist.append(self.trie[letter])

        for node in self.waitlist:
            if letter in node:
                waitlist.append(node[letter])

        self.waitlist = waitlist

        return any('#' in item for item in waitlist)


class StreamChecker2:

    def __init__(self, words: List[str]):
        self.trie = dict()
        for w in words:
            temp_dict = self.trie
            for c in w[::-1]:
                temp_dict = temp_dict.setdefault(c, dict())
            temp_dict['#'] = True

        self.seen = deque()
        self.maxl = max([len(w) for w in words])

    def query(self, letter: str) -> bool:
        self.seen.appendleft(letter)
        if len(self.seen) > self.maxl:
            self.seen.pop()

        cur = self.trie
        for c in self.seen:
            if c in cur:
                cur = cur[c]
                if '#' in cur:
                    return True
            else:
                break
        return False

