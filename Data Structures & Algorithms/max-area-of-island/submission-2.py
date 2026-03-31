class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(row, col):
            area = 0
            q = collections.deque()
            q.append((row, col))
            visit.add((row, col))
            area += 1
            while q:
                r, c = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row,col ) not in visit):
                        q.append((row,col))
                        visit.add((row,col))
                        area += 1
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    maxArea = max(maxArea, bfs(i,j)) 
        return maxArea