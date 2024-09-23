# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        li=[]
        lis=[]
        cur=head
        cur=cur
        while cur:
            li.append(cur.val)
            cur=cur.next
        for i in range(len(li)):
            if i%2==0:
                lis.append(li[i])
        for i in range(len(li)):
            if i%2!=0:
                lis.append(li[i])
        temp=ListNode(lis[0])
        c=temp
        for i in lis:
            c.next=ListNode(i)
            c=c.next
        return temp.next