"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        if not curr: return None
        lDic = {}
        while curr:
            
            lDic[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            newList = lDic[curr]
            newList.next = lDic[curr.next] if curr.next else None
            newList.random = lDic[curr.random] if curr.random else None
            curr = curr.next 
        
        return lDic[head]
           