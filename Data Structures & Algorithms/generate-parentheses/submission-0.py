class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(close, openCount):
            if openCount == close == n:
                res.append("".join(stack))
            
            if openCount < n:
                stack.append('(')
                backtracking(close, openCount + 1)
                stack.pop()
            if close < openCount:
                stack.append(')')
                backtracking(close + 1, openCount)
                stack.pop()




        backtracking(0 ,0)
        return res