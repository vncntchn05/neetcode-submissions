class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        q = deque()

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            i, j, dist = q.popleft()

            for dm, dn in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if i + dm >= 0 and i + dm < m and j + dn >= 0 and j + dn < n and grid[i + dm][j + dn] == 1:
                    q.append((i + dm, j + dn, dist + 1))
                    
            if grid[i][j] == 2:
                continue
            t = max(t, dist)
            grid[i][j] = 2
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return t
        