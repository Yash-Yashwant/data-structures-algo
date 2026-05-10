# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        
        # slow, fast = curr.next, curr.next.next 
        # if i do this i am just skipping the head of the linked list

        # assign the head of the linked list 

        # slow, fast = head, head
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False





        

       

                 

