import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.upper = []  # min heap
        self.lower = []  # max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.upper, num)
        heapq.heappush(self.lower, -heapq.heappop(self.upper))
        if len(self.lower) > len(self.upper):
            heapq.heappush(self.upper, -heapq.heapq.pop(self.lower))

    def findMedian(self) -> float:
        if len(self.upper) == len(self.lower):
            return (self.upper[0] - self.lower[0]) / 2
        else:
            return self.upper[0]
