class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        visit = set()
        q = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i , j))
                    visit.add((i, j))
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
                        visit.add((r,c))
            time += 1
        

        return time if fresh == 0 else -1