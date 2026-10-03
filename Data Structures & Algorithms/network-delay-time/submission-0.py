class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for node, nxtNode, weight in times:
            adj[node].append((nxtNode, weight))

        minHeap = [(0,k)]
        visit = set()
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            time = max(time, w1)
            visit.add(n1)
            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2 + w1, n2])
        return time if len(visit) == n else -1