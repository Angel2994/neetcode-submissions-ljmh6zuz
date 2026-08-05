class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        longest = 0
        for num in count:
            if (num - 1) not in count:
                length = 1
                while (num + length) in count:
                    length += 1
                longest = max(longest, length)

        return longest
