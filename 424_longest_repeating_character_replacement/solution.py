from collections import Counter


def replace(s, k):
    maxf, i = 0, 0
    cnt = Counter()

    for j in range(len(s)):
        cnt[s[j]] += 1
        maxf = max(maxf, cnt[s[j]])

        if j - i + 1 > maxf + k:
            cnt[s[i]] -= 1
            i += 1

    return len(s) - i

