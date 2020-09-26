from solution import Solution


def test_solution():
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert Solution().min_meeting_rooms(intervals) == 2
    assert Solution().min_meeting_rooms_2(intervals) == 2

    intervals = [[7, 10], [2, 4]]
    assert Solution().min_meeting_rooms(intervals) == 1
    assert Solution().min_meeting_rooms_2(intervals) == 1
