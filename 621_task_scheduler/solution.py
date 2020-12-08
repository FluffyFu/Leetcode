from collections import Counter


def task_time(tasks, n):
    cnts = list(Counter(tasks).values())
    max_cnt = max(cnts)
    n_max_cnt = cnts.count(max_cnt)

    t = (max_cnt - 1) * (n + 1) + n_max_cnt

    return max(len(tasks), t)

