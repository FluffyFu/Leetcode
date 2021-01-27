class StockSpanner:

    def __init__(self):
        # mono decreasing
        self.stack = []

    def next(self, price):
        pre_res = 1
        while self.stack and self.stack[-1][0] <= price:
            pre_res += self.stack.pop()[1]

        self.stack.append((price, pre_res))
        return pre_res
