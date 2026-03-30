class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, cols = len(heights), len(heights[0])
        atlanticQ = collections.deque()
        pacificQ = collections.deque()
        for i in range (row):
            pacificQ.append((i, 0))
            atlanticQ.append((i, cols - 1))
        for j in range (cols):
            pacificQ.append((0, j))
            atlanticQ.append((row - 1, j))
        
        def bfs(q):
            visit = set()
            directions = [[1,0],[0,1], [-1,0], [0,-1]]
            while q:
                x, y = q.popleft()
                visit.add((x,y))
                for dl, dr in directions:
                    xx, yy = x + dl,  y + dr
                    if (xx in range (row) and yy in range (cols) and heights[xx][yy] >= heights[x][y] and (xx,yy) not in visit):
                        q.append((xx,yy))
                        visit.add((xx,yy))
            return visit
        pacific = bfs(pacificQ)
        atlantic = bfs(atlanticQ)
        ocean = []
        for r in range (row):
            for c in range (cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    ocean.append([r, c])
        return ocean

