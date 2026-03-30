class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                row, col = q.popleft()
                for dr , dc in directions:
                    a, b = row + dr, col + dc
                    if(a in range(rows) and b in range (cols) and grid[a][b] == '1' and (a,b) not in visit):
                        q.append((a,b))
                        visit.add((a,b))


        for r in range (rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c) 
                    islands += 1
        return islands