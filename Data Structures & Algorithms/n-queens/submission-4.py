class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiag, negDiag = set(), set(), set()
        board = [['.'] * n for i in range(n)]
        res = []
        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c not in cols and (r + c)  not in posDiag and (r - c) not in negDiag:
                    cols.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = 'Q'

                    backtracking(r + 1)

                    cols.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'

        backtracking(0)
        return res