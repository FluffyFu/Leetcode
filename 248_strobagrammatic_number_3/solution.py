from queue import Queue

c_map = {'0': '0',
         '1': '1',
         '6': '9',
         '8': '8',
         '9': '6'}


def find(low, high):
    l = len(low)
    h = len(high)

    if int(low) > int(high):
        return 0

    q = Queue()
    count = 0

    for w in ['', '1', '0', '8']:
        q.put(w)

    while not q.empty():
        cur = q.get()
        if len(cur) >= l and int(cur) >= int(low) and len(cur) <= h and int(cur) <= int(high):
            if cur[0] != '0' or (cur[0] == '0' and len(cur) == 1):
                count += 1

        if h - len(cur) >= 2:
            for w in c_map:
                next_w = w + cur + c_map[w]
                q.put(next_w)
    return count
