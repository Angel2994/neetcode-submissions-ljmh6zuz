class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                l, r = res.pop()
                start = min(intervals[i][0], l)
                end = max(intervals[i][1], r)
                res.append([start, end])
            else:
                res.append(intervals[i])
        return res