class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))


        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 2147483647 and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))
                        grid[row][col] = grid[r][c] + 1