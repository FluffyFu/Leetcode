from typing import List
from collections import Counter, defaultdict
from itertools import chain


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        return [num for _, num in sorted([(f, num) for num, f in counts.items()], reverse=True)[:k]]

    def top_k_frequent_without_sort(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            bucket[-freq].append(num)
        return list(chain(*bucket))[:k]
