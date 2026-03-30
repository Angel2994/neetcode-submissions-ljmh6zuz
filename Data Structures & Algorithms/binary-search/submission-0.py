class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarySearch( start, end):
            if start > end:
                return -1 
            mid = (start + end) // 2
            if  nums[mid] < target:
                return binarySearch(mid + 1, end)
            elif nums[mid] > target:
                return binarySearch(start, mid - 1)
            else:
                return mid
        return binarySearch(0 , len(nums) - 1)
        

         
       
