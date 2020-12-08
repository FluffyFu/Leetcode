def merge_intervals(intervals):
    if not intervals:
        return []
    res = []
    intervals = sorted(intervals, key=lambda x: x[0])
    l, h = intervals[0]

    for intv in intervals[1:]:
        if is_overlap((l, h), intv):
            h = max(h, intv[1])
        else:
            res.append([l, h])
            l, h = intv
    return res


def is_overlap(in1, in2):
    return max(in1[0], in2[0]) >= min(in1[1], in2[1])
