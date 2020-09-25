from solution import Solution, ListNode


def test_solution():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    m = 2
    n = 4

    res = Solution().reverseBetween(head, m, n)
    assert res.val == 1
    assert res.next.val == 4
    assert res.next.next.val == 3
    assert res.next.next.next.val == 2
    assert res.next.next.next.next.val == 5
