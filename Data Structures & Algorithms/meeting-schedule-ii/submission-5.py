"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in range(len(intervals)):
            i1 = intervals[i]
            start.append(i1.start)
            end.append(i1.end)

        start.sort()
        end.sort()
        res, count = 0, 0
        startPtr, endPtr = 0, 0
        while startPtr < len(start):
            if start[startPtr] < end[endPtr]:
                startPtr += 1  
                count += 1
            else:
                endPtr += 1
                count -= 1
            res = max(res, count)
        return res
