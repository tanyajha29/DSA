# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        curr = head
        count = 0

        # set to store and check the connected components
        result_set = set(nums)

        while curr :
            # current node belongs to nums
            if curr.val in result_set :

                # end of cennected nodes
                if curr.next is None or curr.next.val not in result_set :
                    count += 1
            
            curr = curr.next
        
        return count
        