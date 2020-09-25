from solution import Solution, ListNode, SolutionRecursive, SolutionRecursive2
import pudb


def test_solution():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    res = Solution().addTwoNumbers(l1, l2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8


def test_solution_recursive():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # pudb.set_trace()
    res = SolutionRecursive().add_two_numbers(l1, l2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8


def test_solution_recursive_2():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # pudb.set_trace()
    res = SolutionRecursive2().add_two_numbers(l1, l2)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8
