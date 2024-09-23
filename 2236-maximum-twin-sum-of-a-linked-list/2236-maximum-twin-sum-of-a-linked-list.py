# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        i=0
        n=len(li)
        res=[]
        while True:
            if i>(n-1-i):
                break
            res.append(li[i]+li[n-1-i])
            i+=1
        return max(res)