class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for nums in numSet:
            if (nums - 1) not in numSet:
                length = 1
                while (nums + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest