# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        a = []
        while head:
            a.append(head.val)
            head = head.next
        left = 0 
        right = len(a) - 1
        b = []
        while left <= right:
            if left == right:
                b.append(a[left])
            else:
                b.append(a[left])
                b.append(a[right])
            left = left + 1
            right = right - 1
        count = 0
        while dummy:
            dummy.val = b[count]
            dummy = dummy.next
            count = count + 1

