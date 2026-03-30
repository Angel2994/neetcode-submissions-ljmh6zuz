class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        res, resLength = [-1, -1] , float("inf")
        need = len(countT)
        have, l = 0 , 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLength:
                    res = [l , r]
                    resLength = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        res = s[l:r + 1]
        return res
            
