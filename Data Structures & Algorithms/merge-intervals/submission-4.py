class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        
        for i in range(len(intervals)):
            if res and intervals[i][0] <=  res[-1][1]:
                start = min(intervals[i][0], res[-1][0])
                end = max(intervals[i][1], res[-1][1])
                res.pop()
                res.append([start, end])

            else:
                res.append(intervals[i])

        return res