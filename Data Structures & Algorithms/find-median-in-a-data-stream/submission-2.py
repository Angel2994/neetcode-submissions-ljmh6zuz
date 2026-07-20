class MedianFinder:

    def __init__(self):
        self.smallHeap = [] #maxHeap
        self.largeHeap = [] #minHeap

    # O(logn)
    def addNum(self, num: int) -> None:
        
        if self.largeHeap and num > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -num)
            
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -(val))
        
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -(self.smallHeap[0])
        elif len(self.smallHeap) < len(self.largeHeap):
            return self.largeHeap[0]
        else:
            return (-(self.smallHeap[0]) + self.largeHeap[0]) / 2.0
        
        