# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self,root,li):
        if root:
            self.inorder_traversal(root.left,li)
            li.append(root.val)
            self.inorder_traversal(root.right,li)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        self.inorder_traversal(root,li)
        return li