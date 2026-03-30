class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        k = r
        while l <= r:
            hours = 0
            mid = (l + r) // 2
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k