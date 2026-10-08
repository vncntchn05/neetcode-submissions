class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))

        visited = set()

        while q:
            i, j, dist = q.popleft()
            if (i, j) in visited:
                continue

            grid[i][j] = min(dist, grid[i][j])
            visited.add((i, j))
            for dm, dn in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if i + dm >= 0 and i + dm < m and j + dn >= 0 and j + dn < n and grid[i + dm][j + dn] != -1:
                    q.append((i + dm, j + dn, dist + 1))


        