class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        minHeap = []
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        for val in count.keys():
            heapq.heappush(minHeap, val)

        while minHeap:
            minVal = minHeap[0]
            for i in range(minVal, minVal + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

                
                
        return True if not minHeap else False