class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(x, y):
            acc = 0
            grid[y][x] = 0
            for h, v in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if x + h >= 0 and x + h < n and y + v >= 0 and y + v < m and grid[y + v][x + h] == 1:
                    acc += dfs(x + h, y + v)
            return acc + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(j, i))

        return ans
