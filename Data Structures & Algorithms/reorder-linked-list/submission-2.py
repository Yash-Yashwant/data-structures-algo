# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        list1 = head
        # to cater both odd & even number of elements we fast and fast.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        # curr = list2
        #reverse list2
        prev = None 
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 
        first, second = head, prev
        while second:
            temp2 = first.next
            temp3 = second.next
            first.next = second
            second.next = temp2
            first, second = temp2, temp3 
        # return head

