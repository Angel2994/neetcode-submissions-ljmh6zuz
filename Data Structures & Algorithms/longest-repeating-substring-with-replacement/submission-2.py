class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length, l , maxFreq = 0, 0, 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            while (r - l) + 1 - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            length = max(length , (r - l) + 1)
        return length 