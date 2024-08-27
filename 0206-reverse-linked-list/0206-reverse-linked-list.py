# Definition for singly-linked list.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        while cur:
            front=cur.next
            cur.next=prev
            prev=cur
            cur=front
        return prev