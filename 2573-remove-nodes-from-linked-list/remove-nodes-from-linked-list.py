# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        curr=head
        while curr:
            while stack and stack[-1]<curr.val:
                stack.pop()
            stack.append(curr.val)
            curr=curr.next
        if stack:
            dummy=ListNode()
            res=dummy
            for num in stack:
                res.next=ListNode(num)
                res=res.next
            return dummy.next
        else:
            return None




        