class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, cols = len(board), len(board[0])
        q = collections.deque()
        for i in range (cols):
            if (board[0][i] == 'O'):
                q.append((0,i))
            if (board[row-1][i] == 'O'):
                q.append((row-1,i))
        for j in range(row):
            if (board[j][0] == 'O'):
                q.append((j,0))
            if (board[j][cols-1] == 'O'):
                q.append((j,cols-1))
        def bfs():
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            while q:
                x,y = q.popleft()
                board[x][y] = 'T'
                for dl,dr in directions:
                    xx,yy = x + dl, y + dr
                    if(xx in range (row) and yy in range(cols) and board[xx][yy] == 'O'):
                        q.append((xx,yy))
                        board[xx][yy] = 'T'
    
        bfs()
        for i in range (row):
            for j in range (cols):
                if (board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif (board[i][j] == 'T'):
                    board[i][j] = 'O'
