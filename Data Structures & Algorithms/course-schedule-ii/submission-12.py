class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for u, v in prerequisites:
            indeg[u] += 1
            adj[v].append(u)

        ans = []

        def dfs(node):
            ans.append(node)
            indeg[node] -= 1
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    dfs(nei)

        for i in range(numCourses):
            if indeg[i] == 0:
                dfs(i)

        return ans if len(ans) == numCourses else []