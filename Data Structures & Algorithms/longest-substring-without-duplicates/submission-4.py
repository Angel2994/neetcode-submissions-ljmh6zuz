class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l , length = 0, 0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            length = max(length, (r - l) + 1)
        return length 