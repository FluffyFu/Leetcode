import heapq

"""
https://leetcode.com/problems/sliding-window-median/discuss/262689/Python-Small-and-Large-Heaps
"""


def median(nums, k):
    low = []  # lower half maintain a max heap
    high = []  # upper half maintain a min heap

    for i in range(k):
        heapq.heappush(high, (nums[i], i))

    # always keep high equal or larger than low by 1
    for _ in range(k - (k+1)//2):
        v, index = heapq.heappop(high)
        heapq.heappush(low, (-v, index))

    res = []
    res.append(find_m(low, high, k))

    for i in range(k, len(nums)):
        # this part is trick since you want to maintain the heap
        # size and taking care of the lazy deletion at the same time.

        if nums[i] >= high[0][0]:
            heapq.heappush(high, (nums[i], i))
            if nums[i-k] <= high[0][0]:
                move(high, low)
        else:
            heapq.heappush(low, (-nums[i], i))
            if nums[i-k] >= high[0][0]:
                move(low, high)

        while low and low[0][1] <= i-k:
            heapq.heappop(low)

        while high and high[0][1] <= i - k:
            heapq.heappop(high)

        res.append(find_m(low, high, k))

    return res


def move(h1, h2):
    """
    move one element from h1 to h2.
    """
    v, i = heapq.heappop(h1)
    heapq.heappush(h2, (-v, i))


def find_m(low, high, k):
    if k % 2 == 0:
        return (high[0][0] - low[0][0]) / 2
    else:
        return high[0][0]

