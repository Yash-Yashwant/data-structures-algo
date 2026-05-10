# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev=dummy
        rPrev = None 
        curr = head 
        pos = 1
        while pos < left:
            prev = curr
            curr=curr.next
            pos+=1
        leftNode = curr
        while pos <= right:
            temp = curr.next 
            curr.next = rPrev
            rPrev = curr
            curr = temp
            pos+=1
        prev.next = rPrev
        leftNode.next = curr    
                     
        return dummy.next

        

