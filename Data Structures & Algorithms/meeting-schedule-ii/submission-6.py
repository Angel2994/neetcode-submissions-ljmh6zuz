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
            start.append(intervals[i].start)
            end.append(intervals[i].end)

        start.sort()
        end.sort()
        res, count = 0, 0
        l, r = 0, 0
        while l < len(start):
            if start[l] < end[r]:
                count += 1
                l += 1
            else:
                r += 1
                count -= 1
            res = max(res, count)
        return res
