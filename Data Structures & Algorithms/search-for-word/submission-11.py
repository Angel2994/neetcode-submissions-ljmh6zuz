class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()
        def dfs(r, c, i):
            if i == len(word):
                return True

            if r not in range(rows) or c not in range(cols) or word[i] != board[r][c] or (r,c) in visit:
                return False
            if r >= 0 and r <= rows and c >= 0 and c <= cols and board[r][c] == word[i] and (r,c) not in visit:
                visit.add((r,c))
                found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c -1, i + 1))
                visit.remove((r,c))
                return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
            