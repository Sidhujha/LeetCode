# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        head=Node(-1)
        cur=head
        t1=head1
        t2=head2
        carry=0
        while t1 or t2:
            if t1!=None and t2!=None:
                s=t1.val+t2.val+carry
                carry=s//10
                cur.next=Node(s%10)
                cur=cur.next
                t1=t1.next
                t2=t2.next
            
            elif t1==None and t2!=None:
                s=t2.val+carry
                carry=s//10
                cur.next=Node(s%10)
                cur=cur.next
                t2=t2.next
            
            elif t1!=None and t2==None:
                s=t1.val+carry
                carry=s//10
                cur.next=Node(s%10)
                cur=cur.next
                t1=t1.next
        if carry!=0:
            cur.next=Node(carry)
        return head.next