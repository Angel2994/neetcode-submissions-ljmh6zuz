class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        q = collections.deque()
        count = {}
        time = 0
        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        for val in count.values():
            maxHeap.append(-val)
        heapq.heapify(maxHeap)
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            
            if q:
                if q[0][-1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])
        return time
