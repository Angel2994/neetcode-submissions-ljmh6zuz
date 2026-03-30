class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        left = 0
        length = 0
        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            length = max(length, right - left + 1)
        return length