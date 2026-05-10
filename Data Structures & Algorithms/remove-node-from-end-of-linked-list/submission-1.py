# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # finding out the length of the linked list 
        linkList = head 
        count = 0
        while linkList:
            count+=1
            linkList = linkList.next

        dummy = ListNode(0)
        dummy.next = head
        list1 = dummy
        node = 1
        while list1:
            if node <= (count-n):
                list1 =list1.next
                node+=1
            else:
                list1.next = list1.next.next
                return dummy.next 

                