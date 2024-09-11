# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        li=[]
        if root==None:
            return li
        q=[]
        q.append(root)
        while q:
            a=[]
            for i in range(len(q)):
                j=q.pop(0)
                a.append(j.val)
                if j.left:
                    q.append(j.left)
                if j.right:
                    q.append(j.right)
            li.append(a)
        return li