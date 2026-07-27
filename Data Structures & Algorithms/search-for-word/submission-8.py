class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in visit:
                return

           
            visit.add((r,c))
            directions = [[1,0], [0,1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if dfs(row, col, i + 1):
                    
                    return True
            visit.remove((r,c))
            return False


        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0): return True

        return False