from collections import Counter


def scheduler(tasks, n):
    c = Counter(tasks)
    max_cnt = max(c.values())
    n_max_cnt = sum(1 if val == max_cnt else 0 for val in c.values())

    return max(len(tasks), (max_cnt - 1) * (n+1) + n_max_cnt)

