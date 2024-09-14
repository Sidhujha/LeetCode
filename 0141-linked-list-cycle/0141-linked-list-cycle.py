# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow=head
        # fast=head
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        #     if slow==fast:
        #         return True
        # return False
        c=0
        cur=head
        while cur:
            c+=1
            if c>10000:
                return True
            cur=cur.next
