# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =  head = ListNode()
        l1, l2 = list1 , list2
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                
            else:
                
                head.next = l2
                l2 = l2.next
            head = head.next
        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next


        return dummy.next




        
