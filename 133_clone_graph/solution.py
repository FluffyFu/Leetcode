from queue import Queue


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if not node:
        return None
    copy_dict = {node: Node(node.val, [])}

    q = Queue()
    q.put(node)

    while not q.empty():
        cur = q.get()
        for neighr in cur.neighbors:
            if neighr not in copy_dict:
                copy_neighr = Node(neighr.val, [])
                copy_dict[neighr] = copy_neighr
                copy_dict[cur].neighbors.append(copy_neighr)
                q.put(neighr)
            else:
                copy_dict[cur].neighbors.append(copy_dict[neighr])

    return copy_dict[node]

