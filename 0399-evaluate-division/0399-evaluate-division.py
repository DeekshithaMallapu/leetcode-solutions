class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), v in zip(equations, values):
            graph.setdefault(a, {})[b] = v
            graph.setdefault(b, {})[a] = 1 / v

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result

            return -1.0

        return [dfs(a, b, set()) for a, b in queries]