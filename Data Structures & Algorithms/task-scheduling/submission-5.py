class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        maxHeap = []
        for val in count.values():
            maxHeap.append(-val)
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][-1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
