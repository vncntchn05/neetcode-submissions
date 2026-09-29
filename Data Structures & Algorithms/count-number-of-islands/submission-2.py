class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        visited = []
        for i in range(len(grid)):
            visited.append([])
            for j in range(len(grid[0])):
                visited[i].append(0)

        check = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(i, j):
            if visited[i][j] == 1:
                return
            visited[i][j] = 1
            for [m, n] in check:
                if i + m >= 0 and i + m < len(grid) and j + n >= 0 and j + n < len(grid[0]):
                    if grid[i + m][j + n] == "1":
                        if visited[i + m][j + n] != 1:
                            bfs(i + m,j + n)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    grid[i][j] = visited
                    continue
                elif visited[i][j] == 1:
                    continue
                else:
                    ans += 1
                    bfs(i,j)
        
        return ans
