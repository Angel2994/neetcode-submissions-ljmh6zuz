class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for n in nums:
            nextDp = set()
            for t in dp:
                if t + n == target:
                    return True
                nextDp.add(t + n)
                nextDp.add(t)
            dp = nextDp

        return True if target in dp else False