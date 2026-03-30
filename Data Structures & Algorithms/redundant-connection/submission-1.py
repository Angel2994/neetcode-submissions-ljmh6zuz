class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            while (x != par[x]):
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x,y):
            x, y = find(x), find(y)
            if (x == y): return False

            if (rank[x] < rank[y]):
                par[x] = y
                rank[y] += rank[x] + 1
            else:
                par[y] = x
                rank[x] += rank[y] + 1
            return True
        for x,y in edges:
            if not union(x,y):
                return [x,y]
          
        
