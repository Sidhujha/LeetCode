# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1=[]
        leaves2=[]
        def dfs1(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaves1.append(node.val)
            dfs1(node.left)
            dfs1(node.right)
        dfs1(root1)
        def dfs2(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaves2.append(node.val)
            dfs2(node.left)
            dfs2(node.right)
        dfs2(root2)
        if leaves1==leaves2:
            return True