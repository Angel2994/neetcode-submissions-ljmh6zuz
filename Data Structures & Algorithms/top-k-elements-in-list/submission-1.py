class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        a = [[] for i in range(len(nums) + 1)]
        for val, freq in count.items():
            a[freq].append(val)
        res = []
        for i in range(len(a) -1 ,-1, -1):
            for nums in a[i]:
                res.append(nums)
                if len(res) == k:
                    return res
