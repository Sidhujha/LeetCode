# Definition for singly-linked list.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        temp=head
        while temp:
            li.append(temp.val)
            temp=temp.next
        cur=head
        while li:
            cur.val=li.pop()
            cur=cur.next
        return head