class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            p = par[x]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        for x,y in edges:
            if union(x, y):
                n -= 1
        return n