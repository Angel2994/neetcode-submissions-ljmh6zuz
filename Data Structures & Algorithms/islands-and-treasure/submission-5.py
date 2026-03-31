class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        def bfs():
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 2147483647 and (r,c) not in visit:
                        grid[r][c] = grid[row][col] + 1
                        q.append((r,c))
                        visit.add((r,c))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i, j) not in visit:
                    q.append((i,j))
                    visit.add((i,j))
        bfs()