from queue import Queue
from collections import deque


def longest(nums, limit):
    if not nums:
        return 0
    max_q = deque()
    min_q = deque()
    res = 1

    l, r = 0, 0

    while r < len(nums):
        while max_q and nums[r] >= nums[max_q[-1]]:
            max_q.pop()
        while min_q and nums[r] <= nums[min_q[-1]]:
            min_q.pop()

        max_q.append(r)
        min_q.append(r)

        while nums[max_q[0]] - nums[min_q[0]] > limit:
            l += 1
            if l > min_q[0]:
                min_q.popleft()
            if l > max_q[0]:
                max_q.popleft()

        res = max(res, r - l + 1)
        r += 1

    return res

