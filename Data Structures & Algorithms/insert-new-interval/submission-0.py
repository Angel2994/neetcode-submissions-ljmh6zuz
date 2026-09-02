class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        res.append(intervals[0])
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                maxEnd = max(res[-1][1], end)
                res[-1][1] = maxEnd
            else:
                res.append([start, end])

        return res
