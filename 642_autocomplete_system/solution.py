class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = dict()
        for s, time in zip(sentences, times):
            temp = self.trie
            for c in s:
                temp = temp.setdefault(c, dict())
            temp['cnt'] = time

        self.cur_s = ''

        # current node in trie, don't need to go from the root
        # each time.
        self.cur_node = self.trie
        # indicator whether the current search is done
        # no match in trie.
        self.done = False

    def input(self, c: str) -> List[str]:
        if c == '#' and self.cur_s:
            # make sure s is not empty
            temp = self.trie
            for c in self.cur_s:
                temp = temp.setdefault(c, dict())
            temp['cnt'] = temp.get('cnt', 0) + 1

            # reset
            self.cur_s = ''
            self.cur_node = self.trie
            self.done = False
            return []

        self.cur_s += c
        if c in self.cur_node and not self.done:
            # list of (cnt, s)
            self.cur_node = self.cur_node[c]
            res = []
            self.search(self.cur_node, '', res)
            data = sorted(res, key=lambda x: (-x[0], x[1]))
            return [self.cur_s + s[1] for s in data[:3]]
        else:
            self.done = True
            return []

    def search(self, node, path, res):
        if 'cnt' in node:
            res.append((node['cnt'], path))

        if len(node) == 1 and 'cnt' in node:
            # leaf
            return
        for c in node.keys():
            if c != 'cnt':
                self.search(node[c], path+c, res)

