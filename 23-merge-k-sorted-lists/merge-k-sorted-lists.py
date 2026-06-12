# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    # merge two sorted lists
    def mergeTwoLists(self, l1, l2):

        dummy = ListNode(0)

        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:

                tail.next = l1
                l1 = l1.next

            else:

                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # remaining nodes
        if l1:
            tail.next = l1

        else:
            tail.next = l2

        return dummy.next

    def mergeKLists(self, lists):

        if not lists:
            return None

        # keep merging until one list remains
        while len(lists) > 1:

            mergedLists = []

            # merge in pairs
            for i in range(0, len(lists), 2):

                l1 = lists[i]

                # second list may not exist
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedLists.append(
                    self.mergeTwoLists(l1, l2)
                )

            lists = mergedLists

        return lists[0]