# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        fast = head 
        slow = head

        # move fast to the kth position from the beginning
        for i in range(k - 1) :
            fast = fast.next
        
        # store the kth element
        first = fast

        # move fast and slow until end
        # the slow will be at the kth position form the end
        while fast.next :
            slow = slow.next
            fast = fast.next

        # swap the nodes
        first.val, slow.val = slow.val, first.val

        return head
        