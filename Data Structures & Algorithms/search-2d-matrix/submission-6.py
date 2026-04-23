class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break
        
        row = (l + r) // 2
        left, right = 0, cols - 1
        while left <= right:
            m = (left + right) // 2
            if matrix[row][m] < target:
                left = m + 1
            elif matrix[row][m] > target:
                right = m - 1
            else:
                return True
        return False