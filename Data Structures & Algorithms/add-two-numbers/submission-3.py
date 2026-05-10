# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = l1, l2 
        carry = 0
        linkList = []

        while list1 or list2:
            val1 = list1.val if list1 else 0 
            val2 = list2.val if list2 else 0
            sumVal = val1 + val2 + carry
            carry = sumVal//10
            linkList.append(sumVal%10)
            list1, list2 = list1.next if list1 else None, list2.next if list2 else None
        if carry: linkList.append(carry)

        dummy = ListNode(-1)
        list3 = dummy
        for i in linkList:
            list3.next = ListNode(i)
            list3 = list3.next
        return dummy.next

