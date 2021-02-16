class DoubleLinkNode:
    def __init__(self, pre=None, post=None, key=None, val=None):
        self.pre = pre
        self.post = post
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0

        # dummy head and tail
        self.head = DoubleLinkNode()
        self.tail = DoubleLinkNode()
        self.head.post = self.tail
        self.tail.pre = self.head

        # map between key and dll
        self.store = dict()

    def add_node(self, node):
        """
        Add node right after head.
        """
        temp = self.head.post
        self.head.post = node
        node.pre = self.head
        node.post = temp
        temp.pre = node

    def remove_node(self, node):
        """
        remove the given node from linked list.
        """
        node.pre.post = node.post
        node.post.pre = node.pre

    def pop_from_tail(self):
        """
        pop a node from tail (still keep the dummy tail).
        """
        res = self.tail.pre

        res.pre.post = self.tail
        self.tail.pre = res.pre

        return res

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.val = value

            self.remove_node(node)
            self.add_node(node)
        else:
            node = DoubleLinkNode(key=key, val=value)
            self.store[key] = node
            self.add_node(node)
            self.cnt += 1

        if self.cnt > self.capacity:
            node = self.pop_from_tail()
            del self.store[node.key]
            self.cnt -= 1

