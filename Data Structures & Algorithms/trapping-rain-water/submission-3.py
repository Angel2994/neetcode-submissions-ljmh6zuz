class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        water = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                if leftMax - height[l] > 0:
                    water += leftMax - height[l]
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                if rightMax - height[r] > 0:
                    water += rightMax - height[r]
                rightMax = max(rightMax, height[r])
        return water