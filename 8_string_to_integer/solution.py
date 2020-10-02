class Solution:
    MIN = - 2**31
    MAX = 2**31 - 1

    def my_atoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] not in '+-0123456789':
            return 0

        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        else:
            start = 0

        cur = start
        while cur < len(s):
            if s[cur] not in '0123456789':
                break
            cur += 1

        if start == cur:
            return 0

        res = sign * int(s[start: cur])

        if res < self.MIN:
            return self.MIN
        elif res > self.MAX:
            return self.MAX
        else:
            return res

