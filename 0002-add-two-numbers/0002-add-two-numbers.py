# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        s1=s1[::-1]
        s2=s2[::-1]
        s2=int(s1)+int(s2)
        s2=str(s2)[::-1]
        head=ListNode(s2[0])
        cur=head
        for i in s2[1:]:
            cur.next=ListNode(i)
            cur=cur.next
        return head
        