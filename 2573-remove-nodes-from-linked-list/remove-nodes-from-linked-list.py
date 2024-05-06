# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        stack = []

        while prev:
            if stack:
                while stack and stack[-1].val < prev.val:
                    stack.pop()
                if stack:
                    stack[-1].next = prev
                stack.append(prev)
            else:
                stack.append(prev)
            prev = prev.next
        return stack[0]

        