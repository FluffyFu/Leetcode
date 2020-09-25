
from solution import Solution, ListNode


def test_solution():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    assert Solution().detect_cycle(head).val == 2

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    assert Solution().detect_cycle(head).val == 1
