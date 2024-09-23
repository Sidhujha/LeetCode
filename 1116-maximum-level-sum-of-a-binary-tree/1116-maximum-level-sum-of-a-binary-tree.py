# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        li=[]
        q=[]
        q.append(root)
        while q:
            a=[]
            for i in range(len(q)):
                j=q.pop(0)
                a.append(j)
                if j.left!=None:
                    q.append(j.left)
                if j.right!=None:
                    q.append(j.right)
            li.append(a)
        res=[]
        for i in li:
            s=0
            for j in i:
                s+=j.val
            res.append(s)
        m=max(res)
        return res.index(m)+1