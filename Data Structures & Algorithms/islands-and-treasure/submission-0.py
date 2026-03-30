class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols  = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        def bfs():
            
            while q:
                l, r = q.popleft()
                
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dl, dr in directions:
                    ll, rr = l + dl, r + dr
                    if (ll in range (rows) and rr in range (cols) and grid[ll][rr] != -1 and (ll,rr ) not in visit) and grid[ll][rr] == 2147483647:
                        q.append((ll,rr))
                        grid[ll][rr] = grid[l][r] + 1
                        visit.add((ll,rr))
                       
        for i in range (rows):
            for j in range (cols):
                if(grid[i][j] == 0):
                    q.append((i,j))
                    visit.add((i,j))
        bfs()
        


