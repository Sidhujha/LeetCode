# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        cur=head
        for _ in range(n//2-1):
            cur=cur.next
        cur.next=cur.next.next
        return head
        # slow=head
        # fast=head
        # while fast.next and fast.next.next:
        #     slow=slow.next
        #     fast=fast.next.next
        # slow.next=slow.next.next
        # return head