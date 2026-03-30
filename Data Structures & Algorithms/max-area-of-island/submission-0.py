class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            size = 1
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
                        size += 1
            return size

        maxArea = 0
        for r in range (rows):
            for c in range (cols):
                if(grid[r][c] == 1 and (r,c) not in visit):
                    maxArea = max(maxArea, bfs(r,c))
                    
        return maxArea