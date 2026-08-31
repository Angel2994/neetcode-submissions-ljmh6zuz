class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for i, num in enumerate(s):
            count[num] = i

        res = []
        size = 0
        start, end = 0, 0
        for i, num in enumerate(s):
            size += 1
            end = max(end, count[num])
    
            if i == end:
                res.append(size)
                size = 0

        return res