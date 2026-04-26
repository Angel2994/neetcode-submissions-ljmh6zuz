class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1