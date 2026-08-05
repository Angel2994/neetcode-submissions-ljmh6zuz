class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 or (r,c) in visit:
                return 0

            visit.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r, c +  1) + dfs(r - 1, c) + dfs(r, c - 1))
            
        
        for i in range(rows):
            for j in range(cols):
                area = dfs(i, j)
                island = max(island, area)

        return island