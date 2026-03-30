class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l , r = 0 , len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r) // 2
            res = min(res, nums[mid])
            #deffo in left sorted part of array if this true
            if nums[mid] >= nums[l]:
                l = mid + 1
            ## if not we are in the right sorted portion of array but the smallest 
            ## value is gonna be to the left and we dont know what part of sorted
            ## portion we in so we gotta go left 
            else:
                r = mid - 1
        return res
        