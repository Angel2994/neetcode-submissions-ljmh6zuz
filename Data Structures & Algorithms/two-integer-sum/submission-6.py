class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
    
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numMap:
                return [numMap[difference], i]
            numMap[num] = i