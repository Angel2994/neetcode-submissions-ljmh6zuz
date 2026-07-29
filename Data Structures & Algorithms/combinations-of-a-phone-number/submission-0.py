class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res= []
        digitMap = {"2": "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7": "pqrs", "8" : "tuv", "9" : "wxyz"}
        def backtracking(i, combo):
            if len(combo) == len(digits):
                res.append(combo)
                return

            for c in digitMap[digits[i]]:
                backtracking(i + 1, combo + c)

        if digits:
            backtracking(0, "")
        return res
        