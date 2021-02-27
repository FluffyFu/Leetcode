from queue import Queue


def walls(rooms):
    if not rooms:
        return
    nr, nc = len(rooms), len(rooms[0])
    gates = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(nr):
        for j in range(nc):
            if rooms[i][j] == 0:
                gates.append((i, j))

    for i, j in gates:
        q = Queue()
        q.put((i, j, 0))
        seen = set()

        while not q.empty():
            ci, cj, d = q.get()
            for di, dj in dirs:
                ni = ci + di
                nj = cj + dj

                if 0 <= ni < nr and 0 <= nj < nc and (ni, nj) not in seen and rooms[ni][nj] > d+1:
                    rooms[ni][nj] = d + 1
                    q.put((ni, nj, d+1))
                    seen.add((ni, nj))


"""
More efficient, push all the gates into the queue first. This case, each cell is only visited once.
"""


def walls_2(rooms):
    if not rooms:
        return

    nr, nc = len(rooms), len(rooms[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = Queue()
    seen = set()
    for i in range(nr):
        for j in range(nc):
            if rooms[i][j] == 0:
                q.put((i, j, 0))
                seen.add((i, j))

    while not q.empty():
        ci, cj, d = q.get()

        for di, dj in dirs:
            ni = di + ci
            nj = dj + cj

            if 0 <= ni < nr and 0 <= nj < nc and (ni, nj) not in seen and rooms[ni][nj] > 0:
                rooms[ni][nj] = d + 1
                seen.add((ni, nj))
                q.put((ni, nj, d+1))

