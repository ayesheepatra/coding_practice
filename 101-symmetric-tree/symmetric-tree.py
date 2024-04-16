# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ismirror(lnode,rnode):
            if lnode is None and rnode is None:
                return True
            if lnode is None or rnode is None or lnode.val!=rnode.val:
                return False
            return ismirror(lnode.left,rnode.right) and ismirror(lnode.right,rnode.left)
        return ismirror(root,root)
        