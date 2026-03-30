class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for num in range(len(nums)):
            difference = target - nums[num]
            if difference in hashMap:
                return [hashMap[difference], num]

            hashMap[nums[num]] = num
        



