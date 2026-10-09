class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        p, a, visited = set(), set(), set()

        for i in range(m):
            p.add((i, 0))
            a.add((i, n - 1))

        for i in range(n):
            p.add((0, i))
            a.add((m - 1, i))

        def dfs(i, j, s):
            if (i, j) in visited:
                return
            visited.add((i, j))
            if s == "a":
                a.add((i, j))
            if s == "p":
                p.add((i, j))

            for dm, dn in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if i + dm >= 0 and i + dm < m and j + dn >= 0 and j + dn < n:
                    if heights[i + dm][j + dn] >= heights[i][j]:
                        dfs(i + dm, j + dn, s)

        for i, j in list(a):
            dfs(i, j, "a")
        visited = set()
        for i, j in list(p):
            dfs(i, j, "p")

        ans = []
        for i, j in a & p:
            ans.append([i, j])

        return ans