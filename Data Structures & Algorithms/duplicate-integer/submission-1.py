class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = set()
        for num in nums:
            if num in numMap:
                return True
            numMap.add(num)
        return False