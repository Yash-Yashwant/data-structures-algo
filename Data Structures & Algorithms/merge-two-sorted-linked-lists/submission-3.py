# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(-1)
        l1, l2, l3 = list1, list2, list3 

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l3 = l1
                l1 = l1.next
            else:
                l3.next = l2 
                l3 = l2
                l2 = l2.next 
        l3.next = l1 if l1 else l2

        return list3.next
                
