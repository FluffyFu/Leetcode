from queue import Queue


def open_lock(deadends, target):
    deadends = set(deadends)

    if '0000' in deadends:
        return -1
    if '0000' == target:
        return 0

    q = Queue()
    q.put(('0000', 0))
    visited = set()
    visited.add('0000')

    while not q.empty():
        cur, dist = q.get()

        for v in get_neighbor(cur):
            if v == target:
                return dist + 1
            if v not in deadends and v not in visited:
                q.put((v, dist+1))
                visited.add(v)
    return -1


def get_neighbor(s):
    res = []
    for i in range(4):
        if s[i] == '0':
            res.append(s[:i] + '1' + s[i+1:])
            res.append(s[:i] + '9' + s[i+1:])
        elif s[i] == '9':
            res.append(s[:i] + '0' + s[i+1:])
            res.append(s[:i] + '8' + s[i+1:])
        else:
            res.append(s[:i] + str(int(s[i])+1) + s[i+1:])
            res.append(s[:i] + str(int(s[i])-1) + s[i+1:])
    return res

