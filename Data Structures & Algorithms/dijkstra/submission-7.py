class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for node,nxtNode, weight in edges:
            adj[node].append((nxtNode, weight))
        minHeap = [(0, src)]
        res = {}
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in res:
                continue
            res[node] = weight
            for nei, neiWeight in adj[node]:
                if nei not in res:
                    heapq.heappush(minHeap, [weight + neiWeight, nei])
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res