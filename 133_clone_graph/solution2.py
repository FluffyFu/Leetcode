from queue import Queue


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    c_map = {node: Node(node.val)}
    q = Queue()
    q.put(node)

    while not q.empty():
        cur = q.get()
        for v in cur.neighbors:
            if v not in c_map:
                c_v = Node(v.val)
                c_map[v] = c_v
                q.put(v)
            c_map[v].neighbors.append(c_map[cur])

    return c_map[node]

