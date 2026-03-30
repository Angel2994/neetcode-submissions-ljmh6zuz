class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = row - 1
        while top <= bottom:
            row = (top + bottom)// 2
            if target > matrix[row][cols - 1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if not (top <= bottom):
            return False
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False