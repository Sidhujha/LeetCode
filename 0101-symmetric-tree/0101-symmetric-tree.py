# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        li=[]
        q=[root]
        while q:
            a=[]
            nex=[]
            for n in q:
                if n:
                    a.append(n.val)
                    nex.append(n.left)
                    nex.append(n.right)
                else:
                    a.append(-1)
            if any(nex):
                li.append(a)
            else:
                li.append(a)
                break
            q=nex
        for i in li:
            if i!=i[::-1]:
                return False
        return True