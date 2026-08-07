class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        visit = set()
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        time = 0
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r,c))
                directions = [[1,0], [0,1], [-1, 0], [0,-1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row,col) not in visit:
                        grid[row][col] == 2
                        fresh -= 1
                        q.append((row, col))
                        visit.add((row, col))
            time += 1

        return time if fresh == 0 else -1


