class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        res = k
        l , r = 1, k
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res
