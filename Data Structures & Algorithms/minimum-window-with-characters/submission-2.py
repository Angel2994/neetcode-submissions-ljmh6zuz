class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res

        countT , window =  {}, {}
        length, res = float("inf"), [-1, -1]
        l, have= 0, 0
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        need = len(countT)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < length:
                    length = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        res = s[l:r + 1]
        return res
