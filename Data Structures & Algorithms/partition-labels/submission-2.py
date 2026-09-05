class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i, c in enumerate(s):
            count[c] = i

        res = []
        start, end = 0, 0

        for i in range(len(s)):
            end = max(end, count[s[i]])
            if end == i:
                res.append(end - start + 1)
                start = i + 1

        return res