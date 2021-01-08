class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate(head, k):
    n = 0
    cur = head

    while cur:
        n += 1
        cur = cur.next

    if n == 0:
        return head
    k = k % n

    if k == 0:
        return head

    dummy = ListNode(None)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(k):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    new_head = slow.next
    slow.next = None

    cur = new_head
    while cur.next:
        cur = cur.next

    cur.next = dummy.next
    return new_head

