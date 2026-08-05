class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        maxArea = 0
        def bfs(i, j):
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        area += 1
                        q.append((r, c))
                        visit.add((r,c))
            return area



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visit.add((i,j))
                    maxArea = max(maxArea, bfs(i,j))

        return maxArea