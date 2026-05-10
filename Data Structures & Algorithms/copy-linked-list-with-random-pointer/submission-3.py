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
        Dic = {}

        mainList = head
        while mainList:
            Dic[mainList] = Node(mainList.val)
            mainList = mainList.next
        mainList = head
        while mainList:
            Dic[mainList].next = Dic[mainList.next] if mainList.next else None
            Dic[mainList].random = Dic[mainList.random] if mainList.random else None
            mainList = mainList.next
        return Dic[head] if head else None





       