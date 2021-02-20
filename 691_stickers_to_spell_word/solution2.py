from collections import Counter


def min_stickers(stickers, target):
    if not target:
        return 0
    if not stickers:
        return -1

    t_counter = Counter(target)
    sc = [Counter(s) for s in stickers]
    min_cnt = [float('inf')]
    t_chars = set(target)

    back_track(0, min_cnt, t_counter, sc, t_chars)

    return min_cnt[0] if min_cnt[0] != float('inf') else -1


def back_track(cur_cnt, min_cnt, t_counter, sc, t_chars):
    """
    TLE
    """
    if cur_cnt > min_cnt[0]:
        return
    if is_valid(t_counter):
        min_cnt[0] = min(cur_cnt, min_cnt[0])
        return

    for c in t_chars:
        if t_counter[c] <= 0:
            continue
        # need more sticks for this char
        # try all the possible stickers
        for sticker in sc:
            if c not in sticker:
                continue
            # difference caused by the current sticker
            delta = Counter()
            for key in t_counter.keys():
                if key in sticker:
                    delta[key] = min(t_counter[key], sticker[key])
            t_counter -= delta
            back_track(cur_cnt+1, min_cnt, t_counter, sc, t_chars)
            t_counter += delta


def is_valid(t_counter):
    for val in t_counter.values():
        if val > 0:
            return False

    return True
