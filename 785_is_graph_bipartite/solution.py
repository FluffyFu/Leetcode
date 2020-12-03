from queue import Queue


def is_bipartite(graph):
    colors = dict()  # store nodes and its color
    q = Queue()

    for i in range(len(graph)):
        if i not in colors:
            q.put(i)
            colors[i] = 0

            while not q.empty():
                cur = q.get()
                for v in graph[cur]:
                    if v in colors and colors[v] == colors[cur]:
                        return False
                    elif v not in colors:
                        colors[v] = 1 - colors[cur]
                        q.put(v)

    return True

