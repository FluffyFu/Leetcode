from typing import List
import heapq


class Solution:
    """
    Sort the time by its starting time. Maintain a min_heap that stores
    current conflict meeting (thus the heap size is the minimum number of rooms).

    When a new event comes in, we only need to compare its start time and the min_end
    time in heap. If there is a overlap, then the new event must overlap with all the
    event in the heap. Therefore, a new room is needed. We add this new end to the heap.

    If the new event does not overlap with the earliest finish one, we update the earliest finish
    one with the new one (i.e. the new one would use its room).
    """

    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = [intervals[0][1]]

        for start, end in intervals[1:]:
            min_end = heapq.heappop(heap)

            if start >= min_end:
                heapq.heappush(heap, end)

            else:
                heapq.heappush(heap, min_end)
                heapq.heappush(heap, end)

        return len(heap)

    def min_meeting_rooms_2(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = []
        ends = []

        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts = sorted(starts)
        ends = sorted(ends)

        cur_end_index = 0
        n_rooms = 0

        for start in starts:
            if start < ends[cur_end_index]:
                n_rooms += 1
            else:
                cur_end_index += 1

        return n_rooms
