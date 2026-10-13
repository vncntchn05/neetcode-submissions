class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        ans = 0
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                if nei != node:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                ans += 1
            dfs(node)

        return ans
            