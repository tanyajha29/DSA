# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        prev = None
        curr = head

        # reverse the linked list
        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head = prev
        max_seen = head.val
        curr = head

        # check and remove the smaller node
        while curr and curr.next :
            if curr.next.val < max_seen :
                curr.next = curr.next.next
                
            else :
                curr = curr.next
                max_seen = curr.val

        # reverse the linked list back

        prev = None
        curr = head
        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return  prev
        