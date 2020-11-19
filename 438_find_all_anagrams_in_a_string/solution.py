from collections import Counter


class Solution:
    def find_anagrams(self, s, p):
        p = list(p)
        permutations = []
        self.create_permutations(p, permutations, [])
        permutations = set([''.join(val) for val in permutations])

        n = len(p)
        res = []
        for i in range(0, len(s)-n+1):
            if s[i:i+n] in permutations:
                res.append(i)
        return res

    def create_permutations(self, p, res, track):
        if not p:
            res.append(list(track))
            return
        visited = set()
        for i in range(len(p)):
            if p[i] in visited:
                continue
            else:
                visited.add(p[i])
                self.create_permutations(p[:i] + p[i+1:], res, track + [p[i]])

    def find_anagrams_fast(self, s, p):
        if len(s) < len(p):
            return []
        counter = Counter(p)
        slow, fast = 0, 0
        res = []

        for fast in range(0, len(p)):
            if s[fast] in counter:
                counter[s[fast]] -= 1

        if self.is_counter_empty(counter):
            res.append(slow)

        for fast in range(len(p), len(s)):
            if s[slow] in counter:
                counter[s[slow]] += 1
            if s[fast] in counter:
                counter[s[fast]] -= 1

            slow += 1
            if self.is_counter_empty(counter):
                res.append(slow)

        return res

    def is_counter_empty(self, counter):
        for val in counter.values():
            if val != 0:
                return False

        return True


"""
s = 'abcecba' p = 'abc'
counter = {a: 1, b: 1, c: 1}
slow = 0, fast = 0, res = []
fast = 0, s[0]=a, counter = {a: 0, b: 1, c: 1}
fast = 1, s[1]=b, counter = {a: 0, b: 0, c: 1}
fast = 2, s[2]=c, counter = {a: 0, b: 0, c: 0}
res = [0]
fast = 3, s[3] = e, counter = {a: 1, b: 0, c: 0}, slow = 1
fast = 4, s[4] = c, s[1] = b, counter = {a: 1, b: 1, c: -1}, slow = 2
fast = 5, s[5] = b, s[2] = c, counter = {a: 1, b: 0, c: 0}, slow = 3
fast = 6, s[6] = a, s[3] = e, counter = {a: 0, b: 0, c: 0}, slow = 4





create_permutations
p = ['a', 'b', 'c'], res = [], track = []

cp(['a', 'b', 'c'], [], [])
    element = 'a'
    cp(['b', 'c'], [], ['a'])
        element = 'b'
        cp(['c'], [], ['a', 'b'])
            element = 'c'
            cp([], [], ['a', 'b', 'c'])
            res = [['a', 'b' ,'c']]
        p = ['c']
        element = 'c'
        cp(['b'], [['a', 'b', 'c']], ['a', 'c'])
            element = 'b'
            cp([], ['a', 'b', 'c'], ['a', 'c', 'b'])

"""

