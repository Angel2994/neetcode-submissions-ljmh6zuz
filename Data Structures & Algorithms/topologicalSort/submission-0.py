class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        visit = set()
        currPath = set()
        path = []
        def dfs(u):
            if u in visit:
                return True
            if u in currPath:
                return False
            
            currPath.add(u)
            for nei in adj[u]:
                if not dfs(nei):
                    return False
            currPath.remove(u)
            visit.add(u)
            path.append(u)
            return True
        for i in range(n):
            if not dfs(i):
                return []
        path.reverse()
        return path
        
            
