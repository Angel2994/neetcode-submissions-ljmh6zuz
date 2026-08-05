class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        q = collections.deque()
        def bfs(r, c):
            while q:
                r, c = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row in range(rows) and col in range(cols) and grid[row][col] == '1' and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visit:
                    islands += 1
                    q.append((i,j))
                    visit.add((i,j))
                    bfs(i, j)

        return islands

