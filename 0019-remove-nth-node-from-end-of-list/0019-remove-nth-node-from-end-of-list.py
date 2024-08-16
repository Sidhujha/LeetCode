# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None and n==1:
            head=head.next
            return head
        cur=head
        c=0
        while cur is not None:
            c+=1
            cur=cur.next
        if n==c:
            head=head.next
            return head
        cu=head
        for i in range(c-n-1):
            cu=cu.next
        cu.next=cu.next.next
        return head
        