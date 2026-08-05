class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                temperature, index = stack.pop()
                res[index] = i - index

            stack.append((val, i))

        return res