class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        time, fresh = 0,0
        for i in range(row):
            for j in range(cols):
                if (grid[i][j] == 1):
                    fresh += 1
                if(grid[i][j] == 2):
                    q.append((i,j))
                    visit.add((i,j))
        while q and fresh > 0:
            for i in range (len(q)):
                l, r = q.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dl, dr in directions:
                    ll, rr = l + dl, r + dr
                    if(ll in range(row) and rr in range (cols) and (ll,rr) not in visit and grid[ll][rr] == 1):
                        grid[ll][rr] = 2
                        q.append((ll,rr))
                        visit.add((ll,rr))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1