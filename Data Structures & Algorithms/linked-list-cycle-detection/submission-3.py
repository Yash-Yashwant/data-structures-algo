# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle = set()
        linkedList = head

        while linkedList:
            
            if linkedList.next in cycle:
                return True
            cycle.add(linkedList)     
            linkedList =linkedList.next
        return False