class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(x):
            p = par[x]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2: return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for x,y in edges:
            if not union(x,y):
                return [x,y]
