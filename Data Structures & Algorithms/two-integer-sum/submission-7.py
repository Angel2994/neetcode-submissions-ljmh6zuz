class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i, val in enumerate(nums):
            diff = target - val 
            if diff in numSet:
                return [numSet[diff], i]
            numSet[val] = i
        