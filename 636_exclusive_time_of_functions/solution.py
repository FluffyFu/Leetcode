class Solution:
    def exclusive_time(self, n, logs):
        res = [0] * n
        pre_time = 0
        stack = []

        for log in logs:
            f_id, op, time = log.split(':')
            f_id, time = int(f_id), int(time)

            if op == 'start':
                if stack:
                    res[stack[-1]] += time - pre_time
                stack.append(f_id)
                pre_time = time

            elif op == 'end':
                res[stack.pop] += time - pre_time + 1
                pre_time = time + 1
        return res


"""
f_id = 0, op = start, time = 0, stack = [0], pre_time = 0
f_id = 1, op = start, time = 2, res = [2, 0] , stack = [0, 1], pre_time = 2
f_id = 1, op = end, time = 5, res = [2, 4], stack = [0], pre_time = 6
f_id = 0, op = end, time = 6, res = [3, 4], stack = [0], pre_time = 7
"""

