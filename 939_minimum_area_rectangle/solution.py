from collections import defaultdict


def min_area(points):
    seen = set()
    res = float('inf')
    for r1, c1 in points:
        for r2, c2 in seen:
            if (r1, c2) in seen and (r2, c1) in seen:
                res = min(res, abs(r1 - r2) * abs(c1 - c2))
        seen.add((r1, c1))

    return res if res != float('inf') else 0


def min_area2(points):
    nr = len(set(i for i, _ in points))
    nc = len(set(j for _, j in points))

    if nr < 2 or nc < 2:
        return 0

    map_r = defaultdict(list)
    # build a row mapping
    if nr > nc:
        for i, j in points:
            map_r[i].append(j)
    else:
        # build a column mapping
        for i, j in points:
            map_r[j].append(i)

    lastr = {}
    res = float('inf')

    for i in sorted(map_r):
        map_r[i].sort()
        for j1 in range(len(map_r[i])-1):
            for j2 in range(j1+1, len(map_r[i])):
                c1 = map_r[i][j1]
                c2 = map_r[i][j2]
                if (c1, c2) in lastr:
                    res = min(res, (i - lastr[(c1, c2)]) * (c2 - c1))
                lastr[(c1, c2)] = i

    return res if res != float('inf') else 0

