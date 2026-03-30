# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = []
        while head:
            #ts meanas theres a cycle so return true 
            if head.val in visit:
                return True
            else:
                visit.append(head.val)
            head = head.next
        #tis means there was no cycle so return false aka no cycle false means no 
        return False