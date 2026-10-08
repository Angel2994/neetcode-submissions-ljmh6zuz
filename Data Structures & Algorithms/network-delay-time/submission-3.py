class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(n + 1):
            adj[i] = []
        
        for u, v, w in times:
            adj[u].append((v, w))

        visit = set()
        minHeap = [(0, k)]
        time = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, weight)
            for nei, neiWeight in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiWeight + weight, nei])
        return time if len(visit) == n else -1