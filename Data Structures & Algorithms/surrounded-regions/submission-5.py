import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        res = [["X"] * n for _ in range(m)]
        visited = set()

        def dfs(i, j):
            if board[i][j] == "X" or (i, j) in visited:
                return
            res[i][j] = "O"
            visited.add((i, j))
            for dm, dn in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if i + dm >= 0 and i + dm < m and j + dn >= 0 and j + dn < n and board[i + dm][j + dn] == "O" and (i + dm, j + dn) not in visited:
                    dfs(i + dm, j + dn)

        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m - 1][i] == "O":
                dfs(m - 1, i)
        for i in range(1, m - 1):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        
        for i in range(m):
            for j in range(n):
                board[i][j] = res[i][j]