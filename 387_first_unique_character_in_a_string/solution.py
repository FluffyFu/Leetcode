from collections import defaultdict


class Solution:
    def first_unique_char(self, s: str) -> int:
        index_map = defaultdict(list)
        for i, c in enumerate(s):
            index_map[c].append(i)

        res = len(s) + 1
        for index_pos in index_map.values():
            if len(index_pos) == 1 and index_pos[0] < res:
                res = index_pos[0]

        return res if res < len(s) + 1 else -1
