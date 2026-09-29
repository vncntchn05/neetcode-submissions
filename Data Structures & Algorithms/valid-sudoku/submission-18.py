class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        p = True
        for n in range(9):
            r = [False] * 9
            c = [False] * 9
            print(r)
            for i in range(9):
                for j in range(9):
                    if board[i][j] == str(n + 1):
                        if r[i] or c[j]:
                            p = False
                            break
                        else:
                            r[i] = True
                            c[j] = True
                if not p:
                    break
            if not p:
                break
            
            for i in range(3):
                for j in range(3):
                    box = board[3*i][3*j:3*j+3] + board[3*i+1][3*j:3*j+3] + board[3*i+2][3*j:3*j+3]
                    if box.count(str(n + 1)) > 1:
                        p = False

            if not p:
                break

        return p

                