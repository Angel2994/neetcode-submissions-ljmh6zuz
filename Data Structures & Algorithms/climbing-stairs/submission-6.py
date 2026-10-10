class Solution:
    def climbStairs(self, n: int) -> int:
        
        l, r = 1, 1
        for i in range(2, n + 1):
            temp = l + r
            l = r
            r = temp
        return r