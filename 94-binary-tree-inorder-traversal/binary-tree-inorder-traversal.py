# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ls = []

    def dfs(self,root):
        
        if root is None:
            return 
        
        self.inorderTraversal(root.left)
        self.ls.append(root.val)
        self.inorderTraversal(root.right)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.ls



        