class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set ()
        left = 0
        length = 0

        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[left])
                left += 1
            count.add(s[r])
            length = max(length, r - left + 1)
        return length
        