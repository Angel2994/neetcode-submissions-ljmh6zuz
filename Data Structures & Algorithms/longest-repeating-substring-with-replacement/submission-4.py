class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        l, longest = 0, 0
        maxFreq = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r], 0)
            maxFreq = max(maxFreq, charCount[s[r]])
            if (r - l + 1) - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest