from solution import Solution, ListNode, SolutionRecursive


def test_solution():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    res = Solution().reverseList(head)
    assert res.val == 3
    assert res.next.val == 2
    assert res.next.next.val == 1


def test_solution_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    res = SolutionRecursive().reverse_list(head)
    assert res.val == 3
    assert res.next.val == 2
    assert res.next.next.val == 1
