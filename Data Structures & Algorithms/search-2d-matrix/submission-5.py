class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break

        if not (top <= bot): return False

        row = (top + bot) // 2
        l , r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target: return True
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
        return False