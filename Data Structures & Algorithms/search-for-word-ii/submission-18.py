class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()
        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r, c, word, node):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children or (r,c) in visit:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)

            directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc

                dfs(row, col, word, node)
            visit.remove((r,c))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, "", root)

        return list(res)
        