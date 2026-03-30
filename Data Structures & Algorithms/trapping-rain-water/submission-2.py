class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        water = 0
        while l < r:
            if leftmax < rightmax:
                l += 1
                if leftmax - height[l] > 0 :
                    water += leftmax - height[l]
                leftmax = max(leftmax, height[l])
            else:
                r -= 1
                if rightmax - height[r] > 0:
                    water += rightmax - height[r]
                rightmax = max(rightmax, height[r])
        return water