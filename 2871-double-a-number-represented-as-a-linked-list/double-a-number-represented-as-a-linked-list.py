# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            dummy = ListNode()
            current = node
            while current:
                next_node = current.next
                current.next = dummy.next
                dummy.next = current
                current = next_node
            return dummy.next
        head = reverse(head)
        dummy = current = ListNode()
        multiplier = 2  
        carry = 0  
        while head:
            product = head.val * multiplier + carry  
            carry = product // 10  
            current.next = ListNode(product % 10)  
            current = current.next  
            head = head.next  
        if carry:
            current.next = ListNode(carry)
        return reverse(dummy.next)
        