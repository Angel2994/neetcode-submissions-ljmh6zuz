class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        for n in nums:
            oldMax = curMax
            curMax = max(oldMax * n, curMin * n, n)
            curMin = min(oldMax * n, curMin * n, n)
            res = max(res, curMax)

        return res
