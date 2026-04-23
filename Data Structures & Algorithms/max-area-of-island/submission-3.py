class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col))
            visit.add((row, col))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
                        area += 1
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    area = bfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea
