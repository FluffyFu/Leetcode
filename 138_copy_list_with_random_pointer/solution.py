class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next


def copy(head):
    node_map = dict()
    dummy = Node(0)
    cp_pre = dummy

    cur = head
    while cur:
        new_node = Node(cur.val)
        cp_pre.next = new_node
        node_map[cur] = new_node

        cur = cur.next
        cp_pre = new_node

    cur = head
    cp_cur = dummy.next
    while cur:
        cp_cur.random = node_map[cur.random] if cur.random else None
        cur = cur.next
        cp_cur = cp_cur.next

    return dummy.next

