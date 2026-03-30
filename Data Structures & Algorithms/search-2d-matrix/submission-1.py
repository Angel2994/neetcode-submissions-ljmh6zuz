class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][col - 1] < target:
                top = mid + 1
            else:
                break
        if not (top <= bottom): return False
        l = 0
        r = col - 1
        row = (top + bottom) // 2
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False 
