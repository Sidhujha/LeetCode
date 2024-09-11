# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder_traversal(self,root,li):
        if root:
            self.postorder_traversal(root.left,li)
            self.postorder_traversal(root.right,li)
            li.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        self.postorder_traversal(root,li)
        return li