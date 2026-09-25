class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        minDays = r
        while l <= r:
            m = (l + r) // 2
            groups = 1
            currWeight = m
            for num in weights:
                if currWeight - num < 0:
                    groups += 1
                    currWeight = m
                currWeight -= num
                    
            if groups <= days:
                minDays = min(minDays, m)
                r = m - 1
            else:
                l = m + 1

        return minDays