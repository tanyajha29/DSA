# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            # 1. detect cycle
            if slow == fast :
                slow = head

                # 2. find cycle start
                while slow != fast :
                    slow = slow.next
                    fast = fast.next 
                return slow
        return None