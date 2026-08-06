class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacificQ, atlanticQ = collections.deque(), collections.deque()

        for i in range(rows):
            pacificQ.append((i, 0))
            atlanticQ.append((i, cols - 1))

        for j in range(cols):
            pacificQ.append((0, j))
            atlanticQ.append((rows - 1, j))

        def bfs(q):
            visit = set(q)
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1] , [-1,0], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and heights[r][c] >= heights[row][col] and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))

            return visit
        pacificSet = bfs(pacificQ)
        atlanticSet = bfs(atlanticQ)
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacificSet and (i,j) in atlanticSet:
                    res.append([i,j])

        return res
