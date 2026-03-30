class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #create array of size nums, a value can not appear more times then size of nums
        # array[i] = [1,2,3] , [i] is the # of times a value appears = value is 
        array = [[] for i in range( len(nums) + 1)]
        #count frequency, 1 + value, if not in it yet 0 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for value, freq in count.items():
            array[freq].append(value)
        res = []
        #iterate through array backwards, lists could all be in one spot so 
        # but once res == k, you have the result so stop
        for i in range(len(array) - 1, 0, -1):
            for n in array[i]:
                res.append(n)
                if len(res) == k:
                    return res