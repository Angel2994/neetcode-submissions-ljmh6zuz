class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in range(len(s1)):
            count[s1[c]] = 1 + count.get(s1[c], 0)
        l = 0
        compare = {}
        for r in range(len(s2)):
            compare[s2[r]] = 1 + compare.get(s2[r], 0)
            while sum(compare.values()) > sum(count.values()):
                compare[s2[l]] -= 1
                if compare[s2[l]] == 0:  # Remove key if count is zero
                    del compare[s2[l]]
                l += 1
            if count == compare: return True
      
        return False