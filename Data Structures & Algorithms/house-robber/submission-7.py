class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    #rob1 stores the max that we robbed up to two houses ago 
    #rob2 stores the max we robbed up to one house ago 
    #therefore if we rob current house we can only rob that + rob1 or just rob2 and then update our ptrs 