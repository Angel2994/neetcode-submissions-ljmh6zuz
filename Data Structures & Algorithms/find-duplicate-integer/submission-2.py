class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0 , 0
        #cycle detection gimmick 
        #slow fast start at head advance slow by 1 fast by 2 when they intersect
        # stop then run another slow pointer starting from the head 
        # keep original slow ptr , advance both slow ptrs by 1
        # when those intersect you have the answer 
        #Floyd's algorithm 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while nums[slow] != nums[slow2]:
            slow = nums[slow]
            slow2 = nums[slow2]
        return nums[slow]    