# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,pre):
        if root:
            pre.append(root.val)
            self.preorder(root.left,pre)
            self.preorder(root.right,pre)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        self.preorder(root,li)
        return li