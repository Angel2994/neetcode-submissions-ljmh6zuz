class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (row/3, col/3) 9 squares in board can only be one num 1-9 in each square 

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': #skip if empty square
                    continue
                # three edge cases
                # 1. no dupe in col, 2. no dupe in row 3. no dupe in square
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3 , c // 3)].add(board[r][c])
        return True