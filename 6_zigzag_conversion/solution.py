class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        period = self._n_rows_to_period(num_rows)

        if period == 1:
            return s

        res = []
        i = 0

        while i < len(s):
            res.append(s[i])
            i += period

        index_start = 1
        index_end = period - 1

        while index_start < index_end:
            cur_1 = index_start
            cur_2 = index_end
            while cur_1 < len(s) and cur_2 < len(s):
                res.append(s[cur_1])
                res.append(s[cur_2])

                cur_1 += period
                cur_2 += period

            if cur_1 < len(s):
                res.append(s[cur_1])

            index_start += 1
            index_end -= 1

        cur = index_start
        while cur < len(s):
            res.append(s[cur])
            cur += period

        return ''.join(res)

    def _n_rows_to_period(self, num_rows: int) -> int:
        return max(2 * num_rows - 2, 1)
