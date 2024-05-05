# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        dummy=prev=ListNode(next=head)
        while curr:
            while curr.next and curr.val==curr.next.val:
                curr=curr.next
            if prev.next==curr:
                prev=curr
            else:
                prev.next=curr.next
            curr=curr.next
        return dummy.next
        
        