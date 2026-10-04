class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visit = set()
        currPath = set()
        topSort = []
        # we want to call dfs on every node, but before we add it 
        # to the path we want to visit all its descendants
        # once we have gotten to the end then we add to the path 
        # and(mar visited) then we just reverse that and we get the topological sort
        def dfs(node):
            if node in visit:
                return True
            if node in currPath:
                return False
            currPath.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit.add(node)
            currPath.remove(node)
            topSort.append(node)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return topSort