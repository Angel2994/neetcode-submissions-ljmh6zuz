class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacificQ = collections.deque()
        atlanticQ = collections.deque()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        for j in range(cols):
            pacificQ.append((0, j))
            atlanticQ.append((rows - 1, j))
        for i in range(rows):
            pacificQ.append((i, 0))
            atlanticQ.append((i, cols - 1))

        def bfs(q):
            visit = set(q)
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and heights[row][col] <= heights[r][c]:
                        q.append((r,c))
                        visit.add((r,c))
            return visit
        pacific = bfs(pacificQ)
        atlantic = bfs(atlanticQ)
        res = []
        for x in range(rows):
            for y in range(cols):
                if (x,y) in pacific and (x,y) in atlantic:
                    res.append([x,y])
        return res
 