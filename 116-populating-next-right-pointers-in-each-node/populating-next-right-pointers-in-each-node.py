"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        q=deque([root])
        while q:
            previous_node=None
            for i in range(len(q)):
                node=q.popleft()
                if previous_node:
                    previous_node.next=node
                previous_node=node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
        