class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i , h in enumerate(heights):
            startIndex = i
            #can't extend further current height >
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                startIndex = index
            stack.append((startIndex , h ))
        size = len(heights)
        for i, h in stack:
            maxArea = max(maxArea, h * (size - i))
        return maxArea

