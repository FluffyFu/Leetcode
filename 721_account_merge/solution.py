class Solution:
    def account_merge(self, accounts):
        graph = self.build_graph(accounts)
        visited = set()
        res = []

        for acc in accounts:
            name = acc[0]
            subset = []
            email = acc[1]
            if email not in visited:
                self.dfs(graph, email, visited, subset)
                subset = sorted(subset)
                subset.insert(0, name)
                res.append(subset)

        return res

    def build_graph(self, accounts):
        graph = dict()
        for acc in accounts:
            for i in range(1, len(acc)):
                key = acc[i]
                if key not in graph:
                    graph[key] = []
                for email in (acc[1:i] + acc[i+1:]):
                    graph[key].append(email)

        return graph

    def dfs(self, graph, start, visited, subset):
        visited.add(start)
        subset.append(start)
        for v in graph[start]:
            if v not in visited:
                self.dfs(graph, v, visited, subset)
