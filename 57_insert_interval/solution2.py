def insert_interval(intervals, new_interval):
    res = []

    for i, intv in enumerate(intervals):
        if not overlap(intv, new_interval):
            if intv[1] < new_interval[0]:
                res.append(intv)
            else:
                res.append(new_interval)
                res += intervals[i:]
                return res
        else:
            new_interval = [min(intv[0], new_interval[0]),
                            max(intv[1], new_interval[1])]
    res.append(new_interval)
    return res


def overlap(in1, in2):
    return max(in1[0], in2[0]) <= min(in1[1], in2[1])
