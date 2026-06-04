# LinkedList

Placement-focused revision notes for LinkedList.

## Problems

<!-- AUTO-GENERATED START -->

### 203. Remove Linked List Elements (Easy)

🔗 LeetCode Folder: [`203-remove-linked-list-elements`](../203-remove-linked-list-elements)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
       dummy = ListNode(0)
       dummy.next = head
       curr = dummy

       while curr and curr.next :
        # remove the node
        if curr.next.val == val :
            curr.next = curr.next.next
        else :
            curr = curr.next
       return dummy.next
```

### 328. Odd Even Linked List (Medium)

🔗 LeetCode Folder: [`328-odd-even-linked-list`](../328-odd-even-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

### 835. Linked List Components (Medium)

🔗 LeetCode Folder: [`835-linked-list-components`](../835-linked-list-components)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
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
```

### 908. Middle Of The Linked List (Easy)

🔗 LeetCode Folder: [`908-middle-of-the-linked-list`](../908-middle-of-the-linked-list)

- **Pattern:** Linked List
- **Time Complexity:** TBD
- **Space Complexity:** TBD

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # 2 pointers
        # 1 (slow) moves 1 step at a time
        # 2 (fast) moves 2 step at a time

        fast = head
        slow = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        # the slow pointer will end up at the middle only 
        # return slow
        return slow
```

<!-- AUTO-GENERATED END -->
