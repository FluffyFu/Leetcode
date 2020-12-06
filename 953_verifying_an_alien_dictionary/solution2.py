def is_sorted(words, order):
    n_order = 'abcdefghijklmnopqrstuvwxyz'
    map_dict = {}

    for c1, c2 in zip(order, n_order):
        map_dict[c1] = c2

    n_words = []
    for w in words:
        temp = []
        for c in w:
            temp.append(map_dict[c])
        n_words.append(''.join(temp))

    for i in range(len(words)-1):
        if n_words[i] > n_words[i+1]:
            return False

    return True

