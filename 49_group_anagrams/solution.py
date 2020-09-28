from typing import List
from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)
        for s in strs:
            if s == '':
                key = 0
            else:
                key = "".join(sorted(s))
            bucket[key].append(s)

        return [val for val in bucket.values()]

