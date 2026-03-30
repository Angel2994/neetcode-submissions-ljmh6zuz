class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 0
    
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0 )
            maxFreq = max(count.values())
            if (r - l + 1) - maxFreq  <= k:
                longest = max(longest, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1  
        return longest          