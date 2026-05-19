class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / m)
            if hours <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        return k