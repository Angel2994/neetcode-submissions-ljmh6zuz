class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t, 0)

        minHeap = []
        for val in count.values():
            minHeap.append(-val)

        heapq.heapify(minHeap)
        q = collections.deque()
        time = 0
        while minHeap or q:
            time += 1
            if minHeap:
                taskVal = 1 + heapq.heappop(minHeap)
                if taskVal < 0:
                    q.append((time + n, taskVal))
            
            if q and q[0][0] == time:
                heapq.heappush(minHeap, q.popleft()[1])

        return time

