class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for currNode, nxtNode, cost in edges:
            adj[currNode].append((cost, nxtNode))
        minHeap = []
        res = {}
        heapq.heappush(minHeap, [0, src])
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in res:
                continue
            res[node] = cost
            
            for cost2, nei in adj[node]:
                if nei not in res:
                    heapq.heappush(minHeap, [cost + cost2, nei])
                    
        for i in range(n):
            if i not in res:
                res[i] = -1
        return res
