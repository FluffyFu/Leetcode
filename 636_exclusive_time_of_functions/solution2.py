def cal_time(n, logs):
    res = [0] * n
    stack = []
    pre_time = 0

    for l in logs:
        task, label, time = l.split(":")
        time = int(time)

        if label == 'start':
            if stack:
                res[stack[-1]] += (time - pre_time)
            stack.append(int(task))
            pre_time = time
        else:
            res[stack.pop()] += (time - pre_time + 1)
            pre_time = time + 1

    return res

