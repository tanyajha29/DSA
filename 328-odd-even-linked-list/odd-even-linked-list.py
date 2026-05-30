class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next

        # save even list start
        even_head = even

        while even and even.next:

            # connect odd nodes
            odd.next = even.next
            odd = odd.next

            # connect even nodes
            even.next = odd.next
            even = even.next

        # attach even list after odd list
        odd.next = even_head

        return head