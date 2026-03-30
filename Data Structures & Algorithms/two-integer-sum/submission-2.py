class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        res = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashMap:
                res.append(hashMap[difference])
                res.append(i)
                return res
            hashMap[nums[i]] = i

            



