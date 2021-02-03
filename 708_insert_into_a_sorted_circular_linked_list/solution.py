class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head, val):
    if not head:
        head = Node(val)
        head.next = head
        return head
    fast, slow = head, head
    while True:
        if slow.val > slow.next.val:
            break
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if val >= slow.val or val <= slow.next.val:
        temp = slow.next
        slow.next = Node(val)
        slow.next.next = temp
    else:
        cur = slow.next
        while val > cur.val and val > cur.next.val:
            cur = cur.next
        temp = cur.next
        cur.next = Node(val)
        cur.next.next = temp

    return head

