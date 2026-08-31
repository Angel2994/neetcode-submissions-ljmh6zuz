class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)

        l = 0
        r = 0
        res = []
        curChar = set()
        while r < len(s):
            #basically continue increasing window size while the current char is still availabe
            #somewhere
            c = s[r]
            curChar.add(c)
            count[c] -= 1
            if count[c] == 0:
                curChar.remove(c)
            
            if len(curChar) == 0:
                    windowSize = (r - l + 1)
                    l = r + 1
                    res.append(windowSize)
            
            r += 1
        return res