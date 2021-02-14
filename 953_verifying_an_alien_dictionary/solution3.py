def is_sorted(words, order):
    c_map = {}
    s_order = 'abcdefghijklmnopqrstuvwxyz'
    for a, s in zip(order, s_order):
        c_map[a] = s

    for i in range(1, len(words)):
        if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
            return False
        for c1, c2 in zip(words[i-1], words[i]):
            if c_map[c1] < c_map[c2]:
                break
            elif c_map[c1] > c_map[c2]:
                return False
    return True

