class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #conver to max heap by converting all values to negatives
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            # if same values no need to push back
            # if not same then have to squash stones together and push difference
            if stone2 > stone1:
                heapq.heappush(stones, stone1 - stone2)

        return abs(stones[0]) if stones else 0

