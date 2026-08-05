class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacificQ = collections.deque()
        atlanticQ = collections.deque()

        for j in range(cols):
            pacificQ.append((0, j))
            atlanticQ.append((rows - 1, j))
                
        for i in range(rows):      
            pacificQ.append((i, 0))
            atlanticQ.append((i, cols - 1))
        def bfs(q):
            visit = set(q)
            while q:
                r, c = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and heights[r][c] <= heights[row][col] and (row,col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))

            return visit
    
        pacificSet = bfs(pacificQ)
        atlanticSet = bfs(atlanticQ)
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in atlanticSet and (i,j) in pacificSet:
                    res.append([i,j])

        return res
