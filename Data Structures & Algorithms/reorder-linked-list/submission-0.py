# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            # fast is the last node and fast.next tell whether we reached none or not
            slow = slow.next
            fast = fast.next.next
        second = slow.next # assigning the second half list to the second var
        slow.next = None # this break the link to second half and makes it first half

        # reverse the second half 
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge sorted lists
        first, second = head, prev
        while second:
           temp1, temp2 = first.next, second.next
           first.next = second
           second.next = temp1
           first, second = temp1, temp2

        return second
           
            



        
