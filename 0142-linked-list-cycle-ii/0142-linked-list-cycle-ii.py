# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        temp=head
        c=0
        while temp:
            if temp in li:
                return temp
            li.append(temp)
            temp=temp.next
        return None