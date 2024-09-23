# Definition for singly-linked list.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        temp=None
        cur=head
        while cur:
            new=cur.next
            cur.next=temp
            temp=cur
            cur=new
        return temp