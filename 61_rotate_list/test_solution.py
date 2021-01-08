from solution import rotate, ListNode
import pudb


def test():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2

    pudb.set_trace()
    rotate(head, k)

