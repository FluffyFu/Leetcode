class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    return merge_sort(head)


def merge_sort(head):
    if not head:
        return None
    if not head.next:
        return head

    # find the middle point. slow is [n/2] + 1.
    # therefore slow should be the starting point of the second
    # half. so we should use pre to save its previous element.
    # otherwise the recursion is infinite when there are two elements.
    pre = ListNode(0)
    fast = head
    slow = head
    while fast and fast.next:
        pre = slow
        fast = fast.next.next
        slow = slow.next

    pre.next = None
    first = merge_sort(head)
    second = merge_sort(slow)

    dummy = ListNode(0)
    pre = dummy

    while first and second:
        if first.val <= second.val:
            pre.next = first
            first = first.next
        else:
            pre.next = second
            second = second.next
        pre = pre.next

    pre.next = first if first else second

    return dummy.next


def merge_bottom_up(head):
    if not head:
        return head

    cur = head
    cnt = 0

    while cur:
        cur = cur.next
        cnt += 1

    # the size of each merge block
    s = 1

    dummy = ListNode(0)
    dummy.next = head

    # when merge block size is large than the list size, the merge is done.
    while s < cnt:
        cur = dummy.next
        tail = dummy
        while cur:
            # pick are the two block need to merge
            left = cur
            right = split(left, s)

            # head and tail for next loop
            cur = split(right, s)
            tail = merge(left, right, tail)

        s *= 2
    return dummy.next


def split(head, k):
    """
    Returns the head after k step. And cut the linked list there.
    """
    pre = ListNode(0)
    while head and k > 0:
        pre = head
        head = head.next
        k -= 1

    if not head:
        return None

    pre.next = None

    return head


def merge(l1, l2, tail):
    """
    merge l1 and l2, then append the merged result to tail.
    Return the last element of the merged result.
    """
    pre = tail
    while l1 and l2:
        if l1.val <= l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next

    pre.next = l1 if l1 else l2

    while pre.next:
        pre = pre.next

    return pre

