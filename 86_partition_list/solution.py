class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # class ListNode:


def partition(head, x):
    left_head = ListNode(None)
    right_head = ListNode(None)

    left = left_head
    right = right_head

    cur = head
    while cur:
        if cur.val < x:
            left.next = ListNode(cur.val)
            left = left.next
        else:
            right.next = ListNode(cur.val)
            right = right.next

        cur = cur.next

    left.next = right_head.next
    return left_head.next

