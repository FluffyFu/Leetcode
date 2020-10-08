class Solution:
    def max_profit(self, prices):
        if not prices:
            return 0
        res = []
        cur_min = prices[0]
        pre = prices[0]

        for p in prices[1:]:
            if p < pre:
                res.append(pre - cur_min)
                cur_min = p
            else:
                cur_min = min(p, cur_min)
            pre = p

        res.append(pre - cur_min)

        return sum(sorted(res, reverse=True)[:2])


"""
[1, 4, 2, 3]

cur_min = 1, pre = 1

p = 4, res = [], cur_min = 1, pre = 4
p = 2, res = [3], cur_min = 2, pre = 2
p = 3, res = [3], cur_min = 2, pre = 3
"""
