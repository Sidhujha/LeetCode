# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [root.val]
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
            res.append(i[-1].val)
        return res