def add_bold(s, dictionary):
    ins = []
    for i in range(len(s)):
        # last position need to bold (inclusive)
        max_end = -1
        for w in dictionary:
            if s[i:].startswith(w):
                max_end = max(max_end, len(w)+i-1)
        if max_end != -1:
            ins.append([i, max_end])

    # combine intervals:
    if not ins:
        return s
    else:
        c_ins = [ins[0]]
        for cur_in in ins[1:]:
            pre_in = c_ins[-1]

            if pre_in[1] >= cur_in[0] or pre_in[1] + 1 == cur_in[0]:
                c_ins[-1][1] = max(pre_in[1], cur_in[1])
            else:
                c_ins.append(cur_in)

    # add label
    res = []
    pre_end = -1
    for start, end in c_ins:
        res += [s[pre_end+1:start]+'<b>' + s[start:end+1] + '</b>']
        pre_end = end

    res.append(s[end+1:])

    return ''.join(res)

