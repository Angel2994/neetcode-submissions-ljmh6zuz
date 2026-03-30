# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            temp = curr.next ## store next node
            curr.next = prev ## set the next node to previous
            prev = curr ## set the previous node to the next node
            curr = temp ## advance 
        return prev
            
            
