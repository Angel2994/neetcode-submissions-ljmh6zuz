class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, val in enumerate(nums):
            if (target - val) in count:
                return [count[target - val], i]

            count[val] = i