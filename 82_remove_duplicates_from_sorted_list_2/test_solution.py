from solution import Solution, ListNode, SolutionRecursive


def test_solution():
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    new_head = Solution().deleteDuplicates(head)
    assert new_head.val == 2
    assert new_head.next.val == 3


def test_solution_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    new_head = Solution().deleteDuplicates(head)
    assert new_head.val == 1
    assert new_head.next.val == 3


def test_solution_recursive():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    new_head = SolutionRecursive().deleteDuplicates(head)
    assert new_head.val == 1
    assert new_head.next.val == 3


def test_solution_recursive_2():
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)

    new_head = SolutionRecursive().deleteDuplicates(head)
    assert new_head.val == 2
    assert new_head.next.val == 3
