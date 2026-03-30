# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        List3 = temp
        while list1 and list2 != None:
            if list1.val < list2.val:
                List3.next = list1
                list1 = list1.next
            else:
                List3.next = list2
                list2 = list2.next
            List3 = List3.next
        if list1 != None:
            List3.next = list1
        elif list2 != None:
            List3.next = list2
        return temp.next