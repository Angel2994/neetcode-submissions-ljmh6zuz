class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {"2" : "abc", "3" : 'def', "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        res = []
        def backtracking(i, resStr):
            if len(resStr) == len(digits):
                res.append(resStr)
                return

            for char in numMap[digits[i]]:
                backtracking(i + 1, resStr + char)

        if digits:
            backtracking(0, "")
        return res
