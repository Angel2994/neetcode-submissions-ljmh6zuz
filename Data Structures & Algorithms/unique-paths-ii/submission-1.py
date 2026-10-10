class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[rows -1][cols - 1] != 1:
            obstacleGrid[rows - 1][cols - 1] = 1 
        else:
            return 0
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols -1, -1, -1):
                if i == (rows - 1) and j == (cols - 1): continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    bottomRow = obstacleGrid[i + 1][j] if (i + 1) < rows else 0
                    rightCol = obstacleGrid[i][j + 1] if (j + 1) < cols else 0
                    obstacleGrid[i][j] = rightCol + bottomRow
                
        return obstacleGrid[0][0]
