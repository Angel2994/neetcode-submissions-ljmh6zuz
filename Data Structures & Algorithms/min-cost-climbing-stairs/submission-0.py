class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost1 = cost[i] + cost[i + 1]
            cost2 = cost[i] + cost[i + 2]
            cost[i] = min(cost1, cost2)
        
        return min(cost[0], cost[1])