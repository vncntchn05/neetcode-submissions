class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m * n - 1

        while l <= h:
            mid = (l + h) // 2
            r, c = mid // n, mid % n
            print(r)
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                l = mid + 1
            else:
                h = mid - 1
        
        return False
