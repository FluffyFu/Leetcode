from solution import split, ListNode


def test():
    root = ListNode(0)
    a = ListNode(1)
    b = ListNode(2)
    root.next = a
    root.next.next = b

    assert split(root, 1) == a
    assert root.next == None
    assert split(None, 1) == None
    assert split(None, 4) == None
