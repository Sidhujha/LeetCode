# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        li=[]
        temp=head
        while temp:
            if temp in li:
                return True
            li.append(temp)
            temp=temp.next
        return False