class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = collections.deque()
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][cols - 1] == "O":
                q.append((i, cols - 1))
        for j in range(cols):
            if board[0][j] == "O":
                q.append((0,j))
            if board[rows - 1][j] == "O":
                q.append((rows - 1, j))
        
        while q:
            row, col = q.popleft()
            board[row][col] = "Y"
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and board[r][c] == "O":
                    q.append((r,c))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"

            