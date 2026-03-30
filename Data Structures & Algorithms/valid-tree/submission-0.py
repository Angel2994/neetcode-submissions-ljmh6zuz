class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        adj = [[] for i in range(n)] 
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        ## give first node default prev of -1 since start at 0
        ## check len(visit) = n to make sure entire graph is connected
        ## need that for a tree
        return dfs(0,-1) and len(visit) == n
            
        