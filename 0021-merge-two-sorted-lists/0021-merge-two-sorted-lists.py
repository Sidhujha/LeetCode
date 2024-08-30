# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None
        dummy=ListNode(0)
        cur=dummy
        temp1=list1
        temp2=list2
        while temp1 and temp2:
            if temp1.val<temp2.val:
                cur.next=temp1
                cur=cur.next
                temp1=temp1.next
            elif temp1.val>temp2.val:
                cur.next=temp2
                cur=cur.next
                temp2=temp2.next
            elif temp1.val==temp2.val:
                cur.next=temp2
                cur=cur.next
                temp2=temp2.next
        if temp1!=None:
            while temp1:
                cur.next=temp1
                cur=cur.next
                temp1=temp1.next
        if temp2!=None:
            while temp2:
                cur.next=temp2
                cur=cur.next
                temp2=temp2.next
        return dummy.next
        