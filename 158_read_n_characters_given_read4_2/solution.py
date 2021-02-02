def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(self):
        self.buf4 = [''] * 4
        self.i4 = 0  # current pointer in buf4
        self.n4 = 0  # number of char in buf4

    def read(self, buf, n):
        idx = 0

        while idx < n:
            if self.i4 < self.n4:
                buf[idx] = self.buf4[self.i4]
                self.i4 += 1
                idx += 1
            else:
                self.n4 = read4(self.buf4)
                self.i4 = 0
                if not self.n4:
                    return idx
        return idx

