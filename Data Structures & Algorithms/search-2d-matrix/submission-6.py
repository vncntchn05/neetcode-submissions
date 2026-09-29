class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        l = 0
        h = m
        row = 0
        while l <= h:
            mid = (l + h) // 2
            if matrix[mid][0] <= target and matrix[mid][n] >= target:
                row = mid
                break
            elif matrix[mid][0] > target:
                h = mid - 1
            else:
                l = mid + 1

        l = 0
        h = n
        while l <= h:
            mid = (l + h) // 2
            if matrix[row][mid] == target:
                return True
                break
            elif matrix[row][mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        return False
