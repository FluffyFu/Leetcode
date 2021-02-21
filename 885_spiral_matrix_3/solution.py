def spiral(R, C, r0, c0):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    corners = {(0, 0), (0, C-1), (R-1, 0), (R-1, C-1)}
    pos = (r0, c0)
    traj = [pos]
    corner_cnt = 0

    if pos in corners:
        corner_cnt += 1

    move(pos, 0, 1, 0, 0, traj, dirs, R, C, corner_cnt, corners)

    res = []
    for pos in traj:
        if 0 <= pos[0] < R and 0 <= pos[1] < C:
            res.append(list(pos))
    return res


def move(pos, cur_cnt, total, time, head, traj, dirs, R, C, corner_cnt, corners):
    while corner_cnt < len(corners):
        if cur_cnt < total:
            next_pos = (pos[0] + dirs[head][0], pos[1] + dirs[head][1])
            cur_cnt += 1
            traj.append(next_pos)

            if next_pos in corners:
                corner_cnt += 1
            pos = next_pos
        else:
            cur_cnt = 0
            head = (head + 1) % 4

            if time == 0:
                time += 1
            else:
                time = 0
                total = total + 1


def spiral_clean(R, C, r0, c0):
    res = []
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    head = 0
    total_steps = 0

    i, j = r0, c0

    while len(res) < R * C:
        # trick to make range change every other update of total steps
        for _ in range(total_steps//2 + 1):
            if 0 <= i < R and 0 <= j < C:
                res.append([i, j])
            i += dirs[head][0]
            j += dirs[head][1]
        head = (head + 1) % 4
        total_steps += 1

    return res

