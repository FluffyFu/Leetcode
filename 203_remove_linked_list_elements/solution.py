class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_val(head, val):
    dummy = ListNode()

    dummy.next = head
    pre = dummy
    cur = head

    while cur:
        if cur.val == val:
            pre.next = cur.next
            cur = cur.next
        else:
            pre = cur
            cur = cur.next
    return dummy.next

