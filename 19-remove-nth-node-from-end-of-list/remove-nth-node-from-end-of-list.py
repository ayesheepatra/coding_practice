# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr=head
        stemp, temp = None, None
        count=0
        flag = False
        while curr:
            curr = curr.next
            count = count+1
            if count == n:
                flag = True
            
            if flag:
                stemp = temp
                temp = temp.next if temp else head
        # print(stemp.val,temp.val)
        if temp and not stemp:
            return temp.next
        stemp.next=temp.next
        return head
                
    
        