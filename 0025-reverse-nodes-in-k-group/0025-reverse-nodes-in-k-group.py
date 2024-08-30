# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li=[]
        temp=head
        while temp:
            li.append(temp.val)
            temp=temp.next
        if len(li)==0:
            return None
        li1=[]
        i=0
        while i<len(li):
            a=li[i:i+k]
            if len(a)==k:
                a=a[::-1]
                li1.extend(a)
            else:
                li1.extend(a)
            i+=k
        cur=head
        for i in li1:
            cur.next=ListNode(i)
            cur=cur.next
        return head.next