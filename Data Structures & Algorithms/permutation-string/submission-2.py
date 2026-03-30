class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0] * 26
        for c in range(len(s1)):
            count[ord(s1[c]) - ord('a')] += 1 
        l = 0
        compare = [0] * 26
        for r in range(len(s2)):
            compare[ord(s2[r]) - ord('a')] += 1
            while (r - l + 1) > len(s1):
                compare[ord(s2[l]) - ord('a')] -= 1
                
                l += 1
            if count == compare: return True
      
        return False