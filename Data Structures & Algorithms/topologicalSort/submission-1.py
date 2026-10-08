class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        visit = set()
        currPath = set()
        res = []
        def dfs(node):
            if node in visit:
                return True
            if node in currPath:
                return False
            currPath.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            currPath.remove(node)
            visit.add(node)
            res.append(node)
            return True
        for i in range(n):
            if not dfs(i):
                return []
        res.reverse()
        return res