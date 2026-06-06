# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        curr = head
        len = 0

        # find the length of the node
        while curr :
            len += 1
            curr = curr.next
        
        # calculate the length
        base_size = len // k
        extra = len % k

        curr = head
        results = []


        for i in range(k) :
            temp_head = curr

            # current part size
            current_size = base_size
            
            if extra > 0 :
                current_size +=1
                extra -= 1
            
            # move to last node od current
            for j in range(current_size - 1) :
                if curr :
                    curr = curr.next
            
            # Cut linked list after required nodes.
            if curr :
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            results.append(temp_head)
        return results