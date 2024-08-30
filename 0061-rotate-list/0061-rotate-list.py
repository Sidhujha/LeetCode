# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c=1
        temp=head
        while temp.next:
            c+=1
            temp=temp.next
        k=k%c
        cur=head
        for _ in range(c-k-1):
            cur=cur.next
        temp.next=head
        head=cur.next
        cur.next=None
        return head