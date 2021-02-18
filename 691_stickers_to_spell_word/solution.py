from collections import Counter


def min_sticker(stickers, target):
    if not stickers:
        return -1
    if not target:
        return 0

    sc = [Counter(s) for s in stickers]
    min_cnt = [float('inf')]

    back_track(0, min_cnt, 0, Counter(), target, sc)

    return min_cnt[0] if min_cnt[0] != float('inf') else -1


def back_track(cur_cnt, min_cnt, pos, available_chars, target, sc):
    """
    cur_cnt: number of sticks used currently
    min_cnt: list of one element, stores the best result so far.
    pos: cur position in the target.
    available_chars: available characters from the current sticker.
    target: target string
    sc: sticker char counters
    """
    if cur_cnt >= min_cnt[0]:
        # pruning
        return
    if pos == len(target):
        min_cnt[0] = min(min_cnt[0], cur_cnt)
        return

    # check if the current char is in available_chars.
    cur_char = target[pos]
    if cur_char in available_chars and available_chars[cur_char] > 0:
        available_chars[cur_char] -= 1
        back_track(cur_cnt, min_cnt, pos+1, available_chars, target, sc)
        available_chars[cur_char] += 1
    # not found in available_chars, need to add a sticker
    # try all the possible stickers
    else:
        for new_s in sc:
            if cur_char in new_s:
                available_chars += new_s
                back_track(cur_cnt+1, min_cnt, pos,
                           available_chars, target, sc)
                available_chars -= new_s

