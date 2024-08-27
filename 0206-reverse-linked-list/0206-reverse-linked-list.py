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
        newhead=self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead